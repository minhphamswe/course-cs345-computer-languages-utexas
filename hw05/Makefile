REL_DIR = ../tools/ReL
REL_JYTHON = ../tools/ReL/dist/bin/jython
CHECK_DATA = ../tools/ReL/tests/SIMDemo.py
REL_GRAMMAR = ../tools/ReL/grammars/Python.g

check:
	cd $(REL_DIR) && ant
	$(REL_JYTHON) $(CHECK_DATA)

submit:
	turnin ­--submit benself CS345_HW5 Python.g PyTuple.java
