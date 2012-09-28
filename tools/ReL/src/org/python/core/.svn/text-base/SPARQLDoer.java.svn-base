package org.python.core;

import java.sql.ResultSetMetaData;
import java.sql.SQLException;

import net.sf.jsqlparser.JSQLParserException;
import oracle.jdbc.OracleConnection;
import oracle.jdbc.OracleResultSet;
import oracle.jdbc.pool.OracleDataSource;

import java.sql.Statement;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.lang.String;

public class SPARQLDoer {

    public String uname = "";
    public OracleConnection connection;
    
    // the current graph
    public String graph = "http://www.example.org/people.owl";
    
    // the default namespace (or graph) within which full object URIs are resolved
    public String namespace = graph + "#";
    
    // the current model
    public String model = "people";
    
    // A diagnostic dump log of the quads inserted through 
    // insertObject/DataPropQuad calls
    public static BufferedWriter quadDumpOut = null;
    
    // A count of the anon nodes for individuals
    public static int anonNodeIndCount = 0;

    // A count of the anon nodes for model objects
    public static int anonNodeModelCount = 0;

    /**
     * Create a SPARQLDoer to handle interaction with a semantic DB
     * @param url The URL of the DB schema
     * @param uname The user name of the DB schema
     */
    public SPARQLDoer(OracleConnection connection, String uname) {

        this.uname = uname;
        this.model = "RDF_MODEL_" + uname.toUpperCase();
        this.connection = connection;

        try {
        	File quadDumpFile = new File("./tests/quadDump.txt");
        	if (quadDumpFile.exists()) {
        		quadDumpFile.delete();
        	}
        	quadDumpOut = new BufferedWriter(new FileWriter(quadDumpFile, true));
        } catch (IOException e) {
        	e.printStackTrace();
        }
 
    }
    
    public void setNamespace(String namespace) {
    	this.namespace = namespace;
    }
    
    public void setGraph(String graph) {
    	this.graph = graph;
    }
    
    public void setModel(String model) {
    	this.model = model;
    }    
    
    /**
     * Create Sequences, RDF_DATA_TABLE and Model if they don't already exist
     * 
     * @param modelName Model name, usually "RDF_MODEL_" + uname 
     * @throws SQLException
     */
    public void createQuadStore(String modelName) throws SQLException {
        String s = "DECLARE\ncnt NUMBER;\n";
        s += "BEGIN\nSELECT count(*) INTO cnt FROM MDSYS.SEM_MODEL$ WHERE MODEL_NAME = '" + modelName + "';\n";
        s += "IF ( cnt = 0 )\nTHEN\n";
        s += "EXECUTE IMMEDIATE 'CREATE SEQUENCE RDF_DATA_TABLE_SQNC MINVALUE 1 START WITH 1 INCREMENT BY 1 NOCACHE';\n";
        s += "EXECUTE IMMEDIATE 'CREATE SEQUENCE RDF_GUID_SQNC MINVALUE 1 START WITH 1 INCREMENT BY 1 NOCACHE';\n";
        s += "EXECUTE IMMEDIATE 'CREATE TABLE RDF_DATA_TABLE( id NUMBER, triple SDO_RDF_TRIPLE_S)';\n";
        s += "SEM_APIS.CREATE_RDF_MODEL('" + modelName + "', 'RDF_DATA_TABLE', 'triple');\n";
        s += "END IF;\n"; 
        s += "END;\n";
        executeStatement(s);
    }
    
    /**
     * Execute an SQL statement on the database
     * 
     * @param sql An SQL statement 
     * @throws SQLException
     */
    public void executeStatement(String sql) throws SQLException {
        System.out.println("***** NEW STATEMENT: " + sql + "\n***** END NEW STATEMENT\n");
        Statement stmt = null;
        try {
        	stmt = connection.createStatement();
        	stmt.execute(sql);
        } catch (SQLException e) {
            System.out.println(e);
        } finally {
        	if (stmt != null) stmt.close();
        }
    }
    
    /**
     * Execute an SQL query against the DB and return the result set
     * @param query
     * @return
     * @throws SQLException
     * 
     * TODO: Avoid returning resultset, so stmt can be closed cleanly
     */
    public OracleResultSet executeQuery(String query) throws SQLException {
	Statement stmt = null;
	OracleResultSet rs1 = null;
	try {
		stmt = connection.createStatement();
		rs1 = (OracleResultSet) stmt.executeQuery(query);
	} catch (SQLException e) {
		System.out.println("Error executing query: " + query + " : " + e);
	}
	
	return rs1;
    }
    
    /**
     * Insert an ObjectProperty quad statement into the RDF data table
     * 
     * @param subject The subject of the statement  e.g. PERSONT
     * @param property The object-property  e.g. rdf:type
     * @param object The object of the statement  e.g. rdfs:Class
     * @throws SQLException
     */
    public void insertObjectPropQuad(String subject, String property, String object) 
    		throws SQLException {
        String quadName = model + ":<" + this.graph + ">";
    	if (subject.indexOf(":") < 0) {
    		// no specified namespace:  use current default namespace
    		subject = namespace + subject;
    	}
    	if (property.indexOf(":") < 0) {
    		// no specified namespace:  use current default namespace
    		property = namespace + property;
    	}
    	if (object.indexOf(":") < 0) {
    		// no specified namespace:  use current default namespace
    		object = namespace + object;
    	}
    	try {
    		if (quadDumpOut != null) {
    			String s = quadName + "\t" + subject + "\t\t" + property + "\t" + object + "\n";
    			quadDumpOut.write(s);
    			quadDumpOut.flush();
    		}
		} catch (IOException e) {
			e.printStackTrace();
		}
    	String s = 
    			"INSERT INTO RDF_DATA_TABLE VALUES ( RDF_DATA_TABLE_SQNC.nextval, " +
    					"SDO_RDF_TRIPLE_S('" + quadName + "', '" +
    					subject + "', '" + property + "', '" + object + "'))";
    	executeStatement(s);
    }
    
        
    /**
     * Insert a DatatypeProperty quad statement into the RDF data table
     * 
     * @param subject The subject of the statement  e.g. _:i2
     * @param property The object-property  e.g. lastname
     * @param object The object of the statement  e.g. DummyDawer
     * @throws SQLException
     */
    public void insertDataPropQuad(String subject, String property, String object) 
    		throws SQLException {
    	String quadName = model + ":<" + this.graph + ">";
    	if (subject.indexOf(":") < 0) {
    		// no specified namespace:  use current default namespace
    		subject = namespace + subject;
    	}
    	if (property.indexOf(":") < 0) {
    		// no specified namespace:  use current default namespace
    		property = namespace + property;
    	}
    	try {
    		if (quadDumpOut != null) {
    			String s = quadName + "\t\t" + subject + "\t\t" + property + "\t\"" + object + "\"\n";
    			quadDumpOut.write(s);
    			quadDumpOut.flush();
    		}
		} catch (IOException e) {
			e.printStackTrace();
		}
    	String s = 
    			"INSERT INTO RDF_DATA_TABLE VALUES ( RDF_DATA_TABLE_SQNC.nextval, " +
    					"SDO_RDF_TRIPLE_S('" + quadName + "', '" +
						//subject + "', '" + property + "', '" + object + "'))";
    					subject + "', '" + property + "', '\"" + object + "\"'))";
    	executeStatement(s);
    }
    public void insertDataPropQuadSQL(String subject, String property, String object) 
    		throws SQLException {
    	String quadName = model + ":<" + this.graph + ">";
    	if (subject.indexOf(":") < 0) {
    		// no specified namespace:  use current default namespace
    		subject = namespace + subject;
    	}
    	if (property.indexOf(":") < 0) {
    		// no specified namespace:  use current default namespace
    		property = namespace + property;
    	}
    	try {
    		if (quadDumpOut != null) {
    			String s = quadName + "\t\t" + subject + "\t\t" + property + "\t\"" + object + "\"\n";
    			quadDumpOut.write(s);
    			quadDumpOut.flush();
    		}
		} catch (IOException e) {
			e.printStackTrace();
		}
    	String s = 
    			"INSERT INTO RDF_DATA_TABLE VALUES ( RDF_DATA_TABLE_SQNC.nextval, " +
    					"SDO_RDF_TRIPLE_S('" + quadName + "', '" +
						subject + "', '" + property + "', '" + object + "'))";
    					//subject + "', '" + property + "', '\"" + object + "\"'))";
    	executeStatement(s);
    }
    /**
     * Insert DVA Meta Data
     * 
     * @param graphName The context/graph name  e.g. PERSONT
     * @param subject The subject of the statement  e.g. PERSONT
     * @param object The object of the statement  e.g. rdfs:Class
     * @throws SQLException
     */
    public void insertDVAMetaData(String uname, String graphName, String subject, String object) 
    		throws SQLException {
        SPARQLDoer sDoer = new SPARQLDoer(connection, uname);
        sDoer.insertObjectPropQuad(subject, "rdf:type", object);
    }
    
    /**
     * Get the next GUID for this semantic DB.
     * 
     * @return
     * @throws SQLException
     */
    public int getNextGUID() throws SQLException {
        String q = "select RDF_GUID_SQNC.nextval from dual";
        OracleResultSet rs1 = null;
        try {
           rs1 = executeQuery(q);
        } catch (SQLException e) {
                System.out.println(e);
        }
        if (rs1 != null && rs1.next()) return(rs1.getInt(1));
        return(0);
    }
    
    
    
    public String getType(String attr) throws SQLException {
        String q = "select case when a.triple.GET_OBJECT() like '%integer%' then '^^xsd:integer' " +
                               "when a.triple.GET_OBJECT() like '%string%' then '^^xsd:string' " +
			       "when a.triple.GET_OBJECT() like '%decimal%' then '^^xsd:decimal' " +
			       "when a.triple.GET_OBJECT() like '%date%' then '^^xsd:date' " +
                               "else 'unknown' " +
                          "end " +
             "from RDF_DATA_TABLE a where a.triple.GET_SUBJECT() like '%" + attr + "%' and a.triple.GET_PROPERTY() like '%range%'";
        OracleResultSet rs1 = null;
        try {
           rs1 = executeQuery(q);
        } catch (SQLException e) {
                System.out.println(e);
        }
        if (rs1 != null && rs1.next()) return(rs1.getString(1));
        return("unknown");
    }
    
    public String doesClassExist(String className) throws SQLException {
        String q = "select sub from table(\n" + 
                "   sem_match('select * where {\n" + 
                "      ?sub rdf:type rdfs:Class .\n" + 
                "   }',\n" + 
                "	 SEM_MODELS('RDF_MODEL_" + uname + "'), null,\n" + 
                "	 SEM_ALIASES( SEM_ALIAS('', '*')), null) )\n" + 
                "   where sub = '" + className.trim() + "'";
        OracleResultSet rs1 = null;
        try {
           rs1 = executeQuery(q);
        } catch (SQLException e) {
                System.out.println(e);
        }
        if (rs1 != null && rs1.next()) return(rs1.getString(1));
        return(null);
    }
    public String doesColumnExist(String className, String columnName) throws SQLException {
        String q = "select pred from table(\n" + 
                "   sem_match('select * where {\n" + 
                "      :" + columnName + " ?pred rdfs:" + className + " .\n" + 
                "   }',\n" + 
                "	 SEM_MODELS('RDF_MODEL_" + uname + "'), null,\n" + 
                "	 SEM_ALIASES( SEM_ALIAS('', '*')), null) )\n";
        OracleResultSet rs1 = null;
        try {
           rs1 = executeQuery(q);
        } catch (SQLException e) {
                System.out.println(e);
        }
        if (rs1 != null && rs1.next()) return(rs1.getString(1));
        return(null);
    }
    /**
     * Get an anonymous node for an individual,
     * format     _:i123
     * 
     * @return
     * @throws SQLException 
     */
    public String getNextAnonNodeForInd() throws SQLException {
    	return "i" + getNextGUID();
    }
    
    /**
     * Get an anonymous node for a model object
     * i.e. Restriction or class,
     * format     _:m123
     * 
     * @return
     * @throws SQLException 
     */
    public String getNextAnonNodeForModel() throws SQLException {
    	return "_:m" + getNextGUID();
    }
    
    /**
     * Get all attributes as list of short names without namefix prefix (e.g. zipCode)
     * 
     * TODO:  fix the hard coded graph
     * 
     * @param userName
     * @param className
     * @param propTypeName The property type name: "DatatypeProperty" or "ObjectProperty"
     * @return
     * @throws SQLException
     * @throws JSQLParserException
     */
    public List<String> getAllAttributes(String userName, String className, 
    		String propTypeName)    // e.g. "DatatypeProperty" 
    		throws SQLException, JSQLParserException {
    	String q =
    			"select attr from table(sem_match(\n" +
    	        "  'select * where {\n" +
    			"        ?attr rdf:type owl:" + propTypeName + " .\n" +
    			"        ?attr rdfs:domain :" + className + "\n" +
    	        "}',\n" +
    	        "SEM_MODELS('RDF_MODEL_" 
    	        + userName +"'), null,\n" +
    	        "SEM_ALIASES( SEM_ALIAS('', '" 
    	        + namespace + "')), null) )";
    	System.out.println("\nGET ALL DVA ATTRS QUERY:\n" + q);
    	return executeRdfSelect(q);
    }
	public List<String> getAllColumns(String userName, String className) throws SQLException, JSQLParserException {
    	String q =
    			"select col from table(sem_match(\n" +
    	        "  'select * where {\n" +
    			"        ?col rdfs:domain :" + className + " .\n" +
    	        "}',\n" +
    	        "SEM_MODELS('RDF_MODEL_" 
    	        + userName +"'), null,\n" +
    	        "SEM_ALIASES( SEM_ALIAS('', '" 
    	        + namespace + "')), null) )";
    	//System.out.println("\nGET ALL COLUMNS ATTRS QUERY:\n" + q);
    	return executeRdfSelect(q);
    }
    
    /**
     * Get inverse of evaName
     * @param userName
     * @param evaName
     * @return
     * @throws SQLException
     * @throws JSQLParserException
     */
    public void insertEvaValue(String uname, String individual, String attrName, String entity) throws SQLException,
                                                                                                          JSQLParserException {
        String q = "select attr from table(sem_match(\n" +
            "  'select * where {\n" +
            "        :" + attrName + " owl:inverseOf ?attr .\n" +
            "}',\n" +
            "SEM_MODELS('RDF_MODEL_" + uname + "'), null,\n" +
            "SEM_ALIASES( SEM_ALIAS('', '" + namespace + "')), null) )";
        System.out.println("\nGET ALL DVA ATTRS QUERY:\n" +
                q);
        List<String> inverses = executeRdfSelect(q);
        SPARQLDoer sDoer = new SPARQLDoer(connection, uname);
        sDoer.insertObjectPropQuad(individual, attrName, entity);
        for (String inverse : inverses) {
            sDoer.insertObjectPropQuad(entity, inverse, individual);
        }
    }
    
    public List<String> executeRdfSelect(String selectStmt) throws SQLException, JSQLParserException {
        //System.out.println(selectStmt);
        List<String> rowIds = new ArrayList<String>();
        Statement stmt = null;
        try {
        	stmt = connection.createStatement();
        	OracleResultSet rs = (OracleResultSet) stmt.executeQuery(selectStmt);
        	ResultSetMetaData rd = rs.getMetaData();
        	int cc = rd.getColumnCount();
        	//Assumption : 1st column corresponds to tripleId
        	while (rs.next()) {
				rowIds.add(getValue(rs.getString(1)));
        	}
        } finally {
        	if (stmt != null) stmt.close();
        }        	
        return rowIds;
    }
    
    /**
     * 
     * @param selectStmt
     * @param columnLabelMap Maps from the column name to the column label
     * @throws SQLException
     * @throws JSQLParserException
     */
    public void executeAndPrintRdfSelect(String selectStmt, 
    		Map<String, String> columnLabelMap)    
    		throws SQLException, JSQLParserException {
    	
    	Statement stmt = null;
    	try {
    		stmt = connection.createStatement();
    		OracleResultSet rs = (OracleResultSet)stmt.executeQuery(selectStmt);
    		ResultSetMetaData rd = rs.getMetaData();
    		int cc = rd.getColumnCount();
    		System.out.print("\n|");
    		for (int i = 1; i <= cc; i++) {
    			String label = rd.getColumnLabel(i);
    			if (columnLabelMap != null) {
    				String mapdLabel = columnLabelMap.get(label);
    				if (mapdLabel != null) {
    					label = mapdLabel;
    				}
    			}
    			System.out.printf( "%-20s|", label);
    		}
    		System.out.print("\n|");

    		for (int i = 1; i <= cc-1; i++)
    			System.out.printf( "--------------------+");
    		System.out.print("--------------------|\n");
    		while (rs.next()) {
    			System.out.print("|");
    			for (int i = 1; i <= cc; i++) {
    				String columnVal = rs.getString(i);
    				if (columnVal == null) {
    					columnVal = "";
    				}
    				columnVal = columnVal.substring(columnVal.lastIndexOf('/') + 1);
    				//System.out.print(columnVal + "\t");
    				System.out.printf( "%-20s|", columnVal);
    			}
    			System.out.println();
    		}
    		System.out.println("\n");
    	} finally {
    		if (stmt != null) stmt.close();
    	}        	
    }

    private static String getValue(String str) {
        return str.substring(str.lastIndexOf("#") + 1);
    }

	/**
	 * Get members (individuals) of a class, with datatype properties
	 * that match the attr-value pairs provided
	 * 
	 * @param className (optional)
	 * @param attrValues
	 * @return
	 * @throws SQLException
	 * @throws JSQLParserException
	 */
	public List<String> getMembersWithAttrValues(
			String className,
			Map<String, String> attrValues) throws SQLException, JSQLParserException {
		List<String> members = new ArrayList<String>();
		String typeTriple = "";
		if (className != null) {
			typeTriple =  "         ?indiv rdf:type :" + className + " .\n";
		}
		String attrValuesQ = "";
		for (String attr : attrValues.keySet()) {
			attrValuesQ +=
					"?indiv :" + attr + " \"" + attrValues.get(attr).replaceAll("'", "") + "\" .\n";
		}
		String q =
				"select indiv from table(sem_match(\n" +
				"  'select * where {\n" +
				typeTriple +
				attrValuesQ +
				"}',\n" +
				"SEM_MODELS('RDF_MODEL_" 
				+ uname +"'), null,\n" +
				"SEM_ALIASES( SEM_ALIAS('', '" 
				+ namespace + "')), null) )";
		System.out.println("\ngetMembersWithAttrValues: query=\n" + q);
    	members = executeRdfSelect(q);
    	return members;

	}
	
	/**
	 * Get the subject nodes with the supplied attribute value pair.
	 * 
	 * @param attr
	 * @param value
	 * @return
	 * @throws SQLException
	 * @throws JSQLParserException
	 */
	public List<String> getSubjectsWithAttrValue(String attr, String value) throws SQLException, JSQLParserException {
		Map<String, String> attrValues = new HashMap<String, String>();
		return getMembersWithAttrValues(null, attrValues);
	}
    
	public List<String> getObjects(String subject, String property) 
			throws SQLException, JSQLParserException {
		if (subject.indexOf(":") < 0)
			subject = ":" + subject;
		if (property.indexOf(":") < 0)
			property = ":" + property;
		String q =
				"select obj from table(sem_match(\n" +
				"  'select * where {\n" +
				"         " + subject + " " + property + " ?obj" + " .\n" +
				"}',\n" +
				"SEM_MODELS('RDF_MODEL_" 
				+ uname +"'), null,\n" +
				"SEM_ALIASES( SEM_ALIAS('', '" 
				+ namespace + "')), null) )";
		System.out.println("\ngetMembersWithAttrValues: query=\n" + q);
    	List<String> objects = executeRdfSelect(q);
    	return objects;
	}

	/**
	 * Delete all quads with the provided subject and property.
	 * 
	 * @param subject
	 * @param property
	 * @throws SQLException
	 */
	public void deleteQuadsWithSubjectProp(String subject, String property) throws SQLException {
		String q =
				"select obj from table(sem_match(\n" +
				"  'select * where {\n" +
				"         :" + subject + " :" + property + " ?obj" + " .\n" +
				"}',\n" +
				"SEM_MODELS('RDF_MODEL_" 
				+ uname +"'), null,\n" +
				"SEM_ALIASES( SEM_ALIAS('', '" 
				+ namespace + "')), null) )";
        List<String> rowIds = new ArrayList<String>();
        Statement stmt = null;
        Statement stmt2 = null;
        Statement stmt3 = null;
        try {
        	stmt = connection.createStatement();
        	OracleResultSet rs = (OracleResultSet) stmt.executeQuery(q);
        	while (rs.next()) {
        		String obj = getValue(rs.getString(1));
        		String quadName = model + ":<" + graph + ">";
        		String deleteSql = 
        				"DELETE FROM RDF_DATA_TABLE WHERE TRIPLE = SDO_RDF_TRIPLE_S('" +
        		quadName + "', '" +
        		namespace + subject + "', '" + 
        		namespace + property + "', " +
        		"'\"" + obj + "\"')";
        		System.out.println(deleteSql);
        		stmt2 = connection.createStatement();
        		stmt2.execute(deleteSql);
        	}
        } finally {
        	if (stmt != null) stmt.close();
        }  		
		
	}

}

