from NeatPrint import neatPrintTable

print("connecting")
MAKECONNECT URL jdbc:oracle:thin:@rising-sun.microlab.cs.utexas.edu:1521:orcl UNAME cs345_mlp2279 PWORD orcl_mlp2279;
print("dropping tables");
DROP TABLE RDF_DATA;
DROP TABLE RDF_DATA_TABLE;
print (" Executing class definition")

#Class statement
CLASS PERSONT "Persons related to the company" (
personid : INTEGERDATA, REQUIRED;
firstname : STRINGDATA, REQUIRED;
lastname : STRINGDATA, REQUIRED;
zipcode : INTEGERDATA;
spouse "spouse if married" : PERSONT, INVERSE IS spouse;
children "children optional" : PERSONT, INVERSE IS parents;
parents "Persons parents optional" : PERSONT, MV(DISTINCT, MAXVAL 2), INVERSE IS children;
);

#input_var = raw_input("Subclass defintion will execute next")

#Subclass statement
SUBCLASS EMPLT "Current employees of the company" OF PERSONT (
employeeid "Unique employee identification" : INTEGERDATA,REQUIRED;
salary "Current yearly salary" : INTEGERDATA, REQUIRED;
employeemanager "Employee's current manager" : PERSONT,INVERSE IS employeesmanaging;
);

#input_var = raw_input("Insert statements next")
#Inserts

#dva inserts
for num in range(1, 5):
   if num == 1:
      fn = 'Bill'
      ln = 'Dawer'
   elif num == 2:
      fn = 'DummyBill'
      ln = 'DummyDawer'
   elif num == 3:
      fn = 'Kid1'
      ln = 'DummyDawer'
   elif num == 4:
      fn = 'Kid2'
      ln = 'DummyDawer'
   INSERT PERSONT ( personid := num , firstname := fn , lastname := ln , zipcode := 78700 + num);
   
z=10
INSERT INTO PERSONT ( personid, firstname, lastname, zipcode ) VALUES ( 5, 'SQLKid', 'DummyDawer', (lambda x: 78700 + x)(z));


#eva inserts
#input_var = raw_input("EVA Insert statements next")
INSERT PERSONT ( personid := 15 , firstname := "Alice" , lastname := "Dawer" , zipcode := 78705, spouse := PERSONT WITH (firstname = "Bill" AND lastname = "Dawer"), children := PERSONT WITH (firstname = "SQLKid"));

#Subclass inserts:
#input_var = raw_input("Subclass Insert statements next")
INSERT EMPLT FROM PERSONT WHERE firstname = "Bill" AND lastname = "Dawer" ( employeeid:= 101,salary:= 70200 );

#Select All
# input_var = raw_input(" Executing: FROM PERSONT RETRIEVE * WHERE TRUE;")
print "Doing SIM Query"
output=FROM PERSONT RETRIEVE * WHERE TRUE;
neatPrintTable(output)
print "Doing SQL Query"
output=SELECT lastname, personid, firstname, zipcode FROM PERSONT;
neatPrintTable(output)
print

#input_var = raw_input("Modify statements next")

#Modify Statements

#dva modify 
MODIFY LIMIT = 1 PERSONT ( zipcode := 61511 ) WHERE firstname = "Alice" AND lastname = "Dawer";

#eva modify
MODIFY LIMIT = 1 PERSONT ( spouse := PERSONT WITH (firstname = "Bill" AND lastname = "Dawer") ) WHERE firstname = "Alice";

#include

MODIFY LIMIT = 1 PERSONT (children := INCLUDE PERSONT WITH (firstname = "Kid2" )) WHERE firstname = "Alice";

#input_var = raw_input("FROM statements next")

#From Statements

#Select All
# input_var = raw_input(" Executing: FROM PERSONT RETRIEVE * WHERE TRUE;")
output=FROM PERSONT RETRIEVE * WHERE TRUE;
neatPrintTable(output)

#Select All Dvas + EVA - Inverse inferencing
# input_var = raw_input(" Executing: FROM PERSONT RETRIEVE *, firstname OF spouse WHERE TRUE;")
output=FROM PERSONT RETRIEVE *, firstname OF spouse WHERE TRUE;
neatPrintTable(output)

#Select no data
# input_var = raw_input(" Executing: FROM PERSONT RETRIEVE firstname, firstname OF children WHERE firstname = \"Bill\";");
output=FROM PERSONT RETRIEVE firstname, firstname OF children WHERE firstname = "Bill" ;
neatPrintTable(output)

#Select specific data
# input_var = raw_input("FROM PERSONT RETRIEVE firstname, firstname OF children WHERE firstname = \"Alice\";")
output=FROM PERSONT RETRIEVE firstname, firstname OF children WHERE firstname = "Alice";
neatPrintTable(output)

#Select Inferencing - Parents inverse of Children
# input_var = raw_input(" Executing: FROM PERSONT RETRIEVE firstname, firstname OF parents WHERE TRUE;")
output=FROM PERSONT RETRIEVE firstname, firstname OF parents WHERE TRUE;
neatPrintTable(output)

#Select dva of eva - multivalued
# input_var = raw_input(" Executing: FROM PERSONT RETRIEVE firstname OF children  WHERE firstname=\"Alice\";")

output=FROM PERSONT RETRIEVE firstname OF children  WHERE firstname="Alice";
neatPrintTable(output)

output=FROM PERSONT RETRIEVE firstname OF spouse OF children WHERE firstname="Bill";
neatPrintTable(output)

ENTAIL

