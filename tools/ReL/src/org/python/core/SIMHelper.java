package org.python.core;

import java.util.Arrays;

import java.util.List;
import java.util.ArrayList;

import net.sf.jsqlparser.statement.*;
import net.sf.jsqlparser.parser.*;
import net.sf.jsqlparser.statement.select.*;

import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;

import oracle.jdbc.OracleConnection;
import oracle.jdbc.OracleResultSet;
import oracle.jdbc.pool.OracleDataSource;

import java.sql.Statement;

import java.io.StringReader;

import net.sf.jsqlparser.expression.operators.relational.*;
import net.sf.jsqlparser.JSQLParserException;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Collections;
import java.util.Iterator;
import java.util.Map;

import org.python.util.SQLVisitor;

import antlr.StringUtils;

import com.google.common.collect.Lists;

public class SIMHelper {
	
    private String url;
    private String uname;
    private String pword;
    private String website = "http://www.example.org/";
    private OracleConnection connection;
    private Statement stmt;
    private SPARQLDoer sDoer;

    public static class EVAAttribute {
        public String dvaName;
        public List<String> evaAttributeNames;

        public EVAAttribute(String dvaName, List<String> evaAttributeNames) {
            this.dvaName = dvaName;
            this.evaAttributeNames = evaAttributeNames;
        }
    } 
    
    /**
     * Build a SIHHelper to process SIM commands and execute them against a connection to
     * an Oracle semantic DB.
     * 
     * Note:  The connection should not be closed within this class, as it will be closed
     * by its parent (invoker).
     * 
     * @param connection
     * @param uname
     * @param pword
     */
    public SIMHelper(OracleConnection connection, String uname, String pword) {
    	this.connection = connection;
    	this.uname = uname;
    	this.pword = pword;
    	this.sDoer = new SPARQLDoer(connection, uname);
    }

   public String executeFrom(String className, List<String> dvaAttribs, List<String> evaAttribs,
		   Map<String, String> whereAttrValues, String server, String uname, String pword) 
				   throws SQLException, JSQLParserException {
    	
        // If form is EXECUTE FROM PERSONT SELECT *
    	if (dvaAttribs.size() > 0 && dvaAttribs.get(0).equals("*")) {
    		 List<String> allDvas = sDoer.getAllAttributes(uname, className, "DatatypeProperty");
    		 dvaAttribs.remove(0);   // remove "*" element
    		 allDvas.addAll(dvaAttribs);
    		 dvaAttribs = allDvas;
    	}
        
        // assume only a single 'dva OF eva' form, for now
        List<List<String>> evaOfChains = new ArrayList<List<String>>();
        //String dvaOfEva = null;
        // the variable name for the dva e.g. lastnameOFspouse
        //String dvaOfEvaVar = dvaOfEva + "OF" + eva;
        for (String evaAttr : evaAttribs) {
        	// e.g.  ["firstname", "OF", "spouse", "OF", "children"]
        	List<String> evaOfChain = trimAndSplitOnDelim(evaAttr, " ");
        	evaOfChain.removeAll(Collections.singletonList("OF"));
        	Collections.reverse(evaOfChain);
        	evaOfChains.add(evaOfChain);   // e.g.  ["children", "spouse", "firstname"] 

        }
    	
        String colNames = "";
        Map<String, String> colNameToLabelMap = new HashMap<String, String>();
        String qBody = "	?indiv rdf:type :" + className + " .\n";
        for (int i = 0; i < dvaAttribs.size(); i++) {
        	String attrURI = dvaAttribs.get(i);
        	String attrName = getName(attrURI);
        	if (i == 0) {
        		colNames += " " + attrName;	
        	} else {
        		colNames += ", " + attrName;
        	}
        	qBody += "	?indiv :" + attrName + " ?" + attrName + " .\n";
        }
        for (String whereAttr : whereAttrValues.keySet()) {
        	qBody += "	?indiv :" + whereAttr + " \"" + whereAttrValues.get(whereAttr) + "\" .\n";
        }
        if (evaOfChains.size() > 0) {
        	qBody += "   OPTIONAL { \n";
        	int i = -1;
        	for (List<String> evaOfChain : evaOfChains) {  

        		String evaColName = "";      // the retrieval last var name 
        		for (int l = evaOfChain.size()-1; l >= 0; l--) { 
        			evaColName = ((evaColName.length() == 0) ? "" : evaColName + "OF")
        					+ evaOfChain.get(l);
        		}
        		
        		i++;
        		String priorVarName = null;   // previous var
        		String thisVarName = "?x" + i + "_0";
        		// e.g. lastName == "firstnameOFspouseOFchildren"
        		qBody += "      ?indiv :" + evaOfChain.get(0) + " " + thisVarName + " .\n";
        		for (int j = 1; j < evaOfChain.size(); j++) {
        			priorVarName = "x" + i + "_" + (j-1);
        			thisVarName =  "x" + i + "_" + j;
        			if (j == evaOfChain.size()-1) {
        				if (colNames.length() > 0) {
        					colNames += ", ";
        				}
        				colNames += thisVarName;
        				colNameToLabelMap.put(thisVarName.toUpperCase(), evaColName.toUpperCase());
        			}
        			qBody += "      ?" + priorVarName + " :" + evaOfChain.get(j) + " ?" + thisVarName + " .\n";
        		}
        	}
        	qBody += "      } \n";
        }
        String query = "SELECT " + colNames + "\n from table(\n" + 
        		"   sem_match('select * where {\n" + qBody;
        query += "   }',\n" + 
        		"	SEM_MODELS('RDF_MODEL_" + uname + "'), null,\n" + 
        		"	SEM_ALIASES( SEM_ALIAS('', 'http://www.example.org/people.owl#')), null) )";
        System.out.println(query);
        sDoer.executeAndPrintRdfSelect(query, colNameToLabelMap);
        return query;
    }
   
   /**
    * Trim and split String on a delimeter string.
    * 
    * 1. trim leading/trailing spaces
	* 2. split to parts on " "
	* 3. trim each part, removing empty parts
    * 
    * @param s
    * @return trimmed split parts
    */
   private List<String> trimAndSplitOnDelim(String s, String delim) {
	   String r = s.trim();
	   String[] parts = s.split(delim);
	   List<String> parts2 = new ArrayList<String>();
	   for (String part : parts) {
		   part = part.trim(); 
		   if (part.length() > 0) {
			   parts2.add(part);
		   }
	   }
	   return parts2;
   }

	public static EVAAttribute getEvaAttribute(String evaAttributeStr) {
        String[] tokens = evaAttributeStr.split(" of");
        //System.out.println("Num of tokens "+tokens.length);
        List<String> names = new ArrayList<String>();
        for (int i = 1; i < tokens.length; i++)
            names.add(tokens[i].trim());

        EVAAttribute eva = new EVAAttribute(tokens[0].trim(), names);
        //System.out.println("Created attribute "+eva.dvaName+" "+names.size());
        return eva;
    }

    public static void printList(List<String> strings) {
        //String []a = strings.toArray();
        for (int i = 0; i < strings.size(); i++)
            System.out.print(strings.get(i) + " ");
        System.out.println();
    }

    public static String getModelName(String className, String uname) {
        return className + "_" + uname;
    }

    public static String getRulebaseEntry(String className, String uname) {
        return "'" + className + "_" + uname + "_rb'";
    }

    public static String getAliasEntry(String className) {
        return "SEM_ALIAS('" + className + "URI', 'http://www.example.org/" + className + "/')";
    }

    
    public int executeClass(String className, List<String> attributeTypes, List<String> attributeValues, String url,
                            String uname, String pword, int linenumber, int guid, String scname) throws SQLException {

        className = className.toUpperCase().trim();
        String sqlstmt = "";

        String namedGraph = className;
        String modelName = "RDF_MODEL_" + uname.toUpperCase();
        String quadName = modelName + ":<http://www.example.org/" + namedGraph + ">";
        String type = "string";

        sDoer.createQuadStore(modelName);

        sDoer.insertObjectPropQuad(className, "rdf:type", "rdfs:Class");

        if (scname != null) {
            sDoer.insertObjectPropQuad(className, "rdfs:subClassOf", scname.trim());
        }

        for (int i = 0; i < attributeTypes.size(); ++i) {

        	sqlstmt = "";
            String attrType = attributeTypes.get(i).trim();
            if (attrType.equals("ClassComment")) {
            	String value = attributeValues.get(i).substring(1, attributeValues.get(i).length()-1);
            	sDoer.insertDataPropQuad(className, "rdfs:comment", value);

            } else {
            	
            	// e.g. [dva, personid, "Description", INTEGERDATA, REQUIRED]
            	List<String> attrFeatures = trimAndSplitOnDelim(attributeValues.get(i), ":");
            	String dvaOrEva = attrFeatures.remove(0);
            	String attrName = attrFeatures.remove(0);

            	// if this is a description, insert with rdfs:comment
            	String nextFeature = attrFeatures.get(0);
            	if (nextFeature.startsWith("\"") && nextFeature.endsWith("\"")) {
            		String description = nextFeature.substring(1, nextFeature.length()-1);
            		sDoer.insertDataPropQuad(attrName, "rdfs:comment", description);
            		attrFeatures.remove(0);  // pop
            	}

            	if (attrType.equals("dvaAttribute")) {
            		System.out.println("Adding dvaAttribute: " + attrName);

            		//Getting proper type from "INTEGERDATA" e.g. INTEGER
            		String attrRange = attrFeatures.remove(0);
            		type = attrRange.substring(0, attrRange.lastIndexOf("DATA"));
					//Type checking: Have only done integer and string
					if (type.toLowerCase().equals("numeric") || type.toLowerCase().equals("decimal") || type.toLowerCase().equals("real")) {
						type = "xsd:decimal"; // was decimal
					}
					else if (type.toLowerCase().equals("string")) {
						type = "xsd:string"; // was string
					}
					else if (type.toLowerCase().equals("integer")) {
						type = "xsd:integer"; // was integer
					}
					else if (type.toLowerCase().equals("date")) {
						type = "xsd:date"; // was integer
					}
					else {
						type = "xsd:decimal"; // was decimal
					}
            		// if there is no MV present, then assume this is a single-valued attribute
            		boolean multiValued = false;
            		sDoer.insertObjectPropQuad(attrName, "rdf:type", "owl:DatatypeProperty");
            		sDoer.insertObjectPropQuad(attrName, "rdfs:domain", className);
            		sDoer.insertObjectPropQuad(attrName, "rdf:range", "rdfs:" + type);

            		while (attrFeatures.size() > 0) {
            			String attrFeature = attrFeatures.remove(0);
            			if (attrFeature.toLowerCase().contains("mv=")) {
            				multiValued = true;
            				sDoer.insertObjectPropQuad(attrFeatures.get(1), "hasAttr", attrFeature);
            				
            			} else if ("REQUIRED".equals(attrFeature)) {
            				String restriction = sDoer.getNextAnonNodeForModel();
            				sDoer.insertObjectPropQuad(restriction, "rdf:type", "owl:Restriction");
            				sDoer.insertObjectPropQuad(restriction, "owl:onProperty", attrName);
            				sDoer.insertDataPropQuad(restriction, "owl:qualifiedCardinality", "1");
            				sDoer.insertObjectPropQuad(restriction, "owl:onDataRange", "xsd:nonNegativeInteger");
            				sDoer.insertObjectPropQuad(className, "rdfs:subClassOf", restriction);
            			}
            		}
            		if (! multiValued) {
            			sDoer.insertObjectPropQuad(attrName, "rdf:type", "owl:FunctionalProperty");
            		}

            	} else if (attrType.equals("evaAttribute")) {

            		System.out.println("Inserting evaAttribute: ");
            		String range = attrFeatures.remove(0);
					boolean multiValued = false;
            		sDoer.insertObjectPropQuad(attrName, "rdf:type", "owl:ObjectProperty");
            		sDoer.insertObjectPropQuad(attrName, "rdfs:domain", className);
            		sDoer.insertObjectPropQuad(attrName, "rdfs:range", range);

            		while (attrFeatures.size() > 0) {
            			String attrFeature = attrFeatures.remove(0);
            			if (attrFeature.toLowerCase().contains("inverseis")) {
            				String[] inverseArray = attrFeature.split("=");
            				String inverseIs = inverseArray[1];
            				sDoer.insertObjectPropQuad(attrFeature, "owl:inverseOf", inverseIs);
            				sDoer.insertObjectPropQuad(inverseIs, "owl:inverseOf", attrName);
            			} else if (attrFeature.toLowerCase().contains("mv=")) {
            				multiValued = true;
            				sDoer.insertObjectPropQuad(attrName, "hasAttr", attrFeature);
            			}
            		}
            		if (! multiValued) {
            			sDoer.insertObjectPropQuad(attrName, "rdf:type", "owl:FunctionalProperty");
            		}
            	}
            }
        }
        return linenumber;
    }

    
    public int executeInsert(String className, List<String> attributeNames, List<String> attributeValues,
                             String fromClause, String url, String uname, String pword, int linenumber,
                             int guid) throws SQLException, JSQLParserException {

        className = className.toUpperCase().trim();
        String individual = null;

        if (fromClause != null && fromClause.length() > 0) {
            // e.g. fromClause == "FROM  PERSONT  WHERE firstname  Bill  lastname  Dawer"  (doubly spaced !!)
            // e.g. fromParts == ["FROM", " ", "PERSONT", " ", "WHERE", "firstname", " ", "Bill", " ", "lastname", " ", "Dawer"]
            List<String> fromParts = trimAndSplitOnDelim(fromClause, " ");

            String superClass = fromParts.get(1);
            Map<String, String> attrValues = new HashMap<String, String>();
            for (int i = 3; i < fromParts.size(); i = i + 2) {
                attrValues.put(fromParts.get(i), fromParts.get(i + 1));
            }
            List<String> individuals = sDoer.getMembersWithAttrValues(superClass, attrValues);
            if (individuals.size() > 0) {
                individual = individuals.get(0); // should only be one
            }

        } else {
            individual = sDoer.getNextAnonNodeForInd();
        }

        // sDoer.insertDVAMetaData("", individual, className);
        sDoer.insertObjectPropQuad(individual, "rdf:type", className);

        System.out.println("Inserting attributes\n");

        for (int i = 0; i < attributeNames.size(); ++i) {
            String attrName = attributeNames.get(i);
            String attrValue = attributeValues.get(i).trim();
            if (attrValue.contains("WITH")) {
                // e.g. "PERSONT WITH   firstname DummyBill zipcode 78705]
                String[] withParts =
                    attrValue.split("\\s+"); // e.g. [PERSONT, WITH, firstname, DummyBill, zipcode, 78705]				
                String withClass = withParts[0];
                Map<String, String> attrValues = new HashMap<String, String>();
                for (int j = 2; j < withParts.length; j = j + 2) {
                    String attr = withParts[j];
                    String value = withParts[j + 1];
                    attrValues.put(attr, value);
                }
                List<String> members = sDoer.getMembersWithAttrValues(withClass, attrValues);
                
                // if members > 1 and attr is a FunctionalProp, report error and abandon member inserts
                List<String> attrTypes = sDoer.getObjects(attrName, "rdf:type");
                if (attrTypes.contains("FunctionalProperty") && (members.size() > 1)) {
                	System.err.println("ERROR: Can't assign results of WITH clause: " + attrValue +
                			" to property: " + attrName + " since there are too many values: " + members);
                	break;
                }
                
                for (String member : members) {
                    sDoer.insertEvaValue(uname, individual, attrName, member);
                }

            } else {
				//////////////////////////////////////////
				String dataType = sDoer.getType(attrName);
				// this if statement removes the leading and trailing single quotes from strings and dates
				if (dataType.endsWith("string")) {
					attrValue = "\"" + attrValue + "\"" + dataType;
				} else if (dataType.endsWith("date")) {
					if (attrName.toUpperCase().equals("NULL") || attrName.equals("''")) {
						attrValue = "NULL" + dataType;
					} else {
						attrValue = "\"" + attrValue + "\"" + dataType;
					}
				} else if (dataType.endsWith("unknown")) {
					attrValue = attrValue.replaceAll("'", "");
				} else {
					attrValue = "\"" + attrValue + "\"" + dataType;
				}
                // TODO: determine type of object
                sDoer.insertDataPropQuadSQL(individual, attrName, attrValue);
            }
        }
        return linenumber;
    }


    public void executeModify(String className, Map<String, String> attributeValues,
                                     Map<String, String> whereAttrValues, int limit, 
                                     String url, String uname, String pword,
                                     int linenumber, int guid) throws SQLException, JSQLParserException {
        
        className = className.toUpperCase().trim();
        List<String> indivs = sDoer.getMembersWithAttrValues(className, whereAttrValues);

        if (indivs.size() > limit) {
            throw new SQLException("Limit exceeded. Allowed " + limit + ". Found " + indivs.size() + " inidividuals");
        }

        for (String indiv : indivs) {
        	for (String attr : attributeValues.keySet()) {
        		String value = attributeValues.get(attr);
        		if (value.contains("WITH")) {
        			// Process value of form "PERSONT WITH   firstname Bill  lastname Dawer"
        			List<String> parts = trimAndSplitOnDelim(value, " ");
        			String modifier = null;
        			if (parts.get(0).equals("INCLUDE") ||
        					(parts.get(0).equals("EXCLUDE"))) {
        				modifier = parts.get(0);
        				parts = parts.subList(1, parts.size());
        			}
        			String withClass = parts.get(0);
        			Map<String, String> withAttrVals = new HashMap<String, String>();
        			for (int i = 2; i < parts.size(); i = i + 2) {
        				withAttrVals.put(parts.get(i), parts.get(i+1));
        			}
        			List<String> valuesToAdd = sDoer.getMembersWithAttrValues(withClass, withAttrVals);
        			List<String> originalValues = new ArrayList<String>();
        			// if this is an EXCLUDE, remember original values
                                if (modifier != null) {
                                    if (modifier.equals("EXCLUDE")) {
                                            originalValues = sDoer.getObjects(indiv, attr);
                                            originalValues.removeAll(valuesToAdd);
                                            valuesToAdd = originalValues;
                                    }
                                    // if INCLUDE, add to original values:  don't delete originals
                                    if (! modifier.equals("INCLUDE")) {
                                            sDoer.deleteQuadsWithSubjectProp(indiv, attr);
                                    }
                                }
        			for (String valueIndiv : valuesToAdd) {
        				sDoer.insertEvaValue(uname, indiv, attr, valueIndiv);
        			}
        		} else {
        			// not WITH:  single dva value
        			sDoer.deleteQuadsWithSubjectProp(indiv, attr);
        			sDoer.insertDataPropQuad(indiv, attr, value);
        		}
        	}
        }
    }
    
    private static String getName(String str) {
        return str.substring(str.lastIndexOf("#") + 1);
    }
    
}

