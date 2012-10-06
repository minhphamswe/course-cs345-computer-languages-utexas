Parser.class: Parser.java
	javac *.java

Parser.java: Parser.jj
	javacc $<

clean:
	rm -f *.class *.java

submit:
	turnin ­--submit benself CS345_HW4 HW4.scm HW4.rkt Parser.jj
