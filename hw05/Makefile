REL_DIR = ../tools/ReL
REL_JYTHON = ../tools/ReL/dist/bin/jython
CHECK_DATA = ../tools/ReL/tests/SIMDemo.py
REL_GRAMMAR = ../tools/ReL/grammars/Python.g
REL_PYTUPLE = ../tools/ReL/src/org/python/core/PyTuple.java

check:
	cd $(REL_DIR) && ant
	$(REL_JYTHON) $(CHECK_DATA)

submit:
	cp $(REL_GRAMMAR) ./
	cp $(REL_PYTUPLE) ./
	turnin ­--submit benself CS345_HW5 Python.g PyTuple.java
