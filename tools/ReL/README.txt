A SParqly Jython++ 
by Cliffy Cheng, Francisco Garcia, and Carlos Urrutia
===============================

--------------------------------------------
What it is:
--------------------------------------------
Improving ASPJython++ by incorporating homeworks. (SPARQL not fully supported, joins, update, delete, etc,.)
Added syntax to be allow conversion of a RDF database into ASP/Prolog facts by returning a Tuple.
Added syntax to be able to create RDF table from SQL table, using the Tuple as the return type.
Use of Oracle Sequence as a GUID.

--------------------------------------------
Steps to compile and run:
--------------------------------------------
1. Download a new Jython source.
2. Download and compile a Grounder and Solver.
We used Gringo and Clasp, you can download them at http://potassco.sourceforge.net/
(We have provided Gringo and Clasp which works in Windows(Cygwin), if that does not work download them from
link provided above)

3. Replace existing Jython files with the A SParqly Jython++ files.

4. Change the directory of the Grounder and Solver in PyTuple.java to point to your compiled executable for each by editing the variables String Grounder on line 76 and String Solver on line 77.

5. Using the ant command, compile A SParqly Jython++

6. Run A SParqly Jython++ from ./dist/bin/jython


--------------------------------------------
Acceptable input:
--------------------------------------------
To know about ASP and Prolog acceptable input, view READMEASPJ.rtf(original project: ASPJylog++)

ASPSELECT * FROM SOMETABLE;
RDFSELECT * FROM SOMETABLE;
--------------------------------------------
Examples:
--------------------------------------------
Example of how to use ASPSELECT is given on the tests/demoDiners.py, and tests/demoBells.
To see how RDFSELECT works see tests/demoRDF.py
To verify Oracle sequence works just close jython, then INSERT to a already created table, note that
the guid changes.

To run them just use:

dist/bin/jython tests/demo<which ever>.py


