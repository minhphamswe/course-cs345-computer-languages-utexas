all: Parser.class

Parser.class: Parser.java
	javac *.java

Parser.java: Parser.jj
	javacc $<

clean:
	rm -f *.class *.java
	rm -f .fuse_hidden*
	rm -f *~

check: all
	echo "(0'' 0''' mult)" | java Parser

submit:
	make clean
	rm -f fas.zip
	zip -r fas.zip ./
	turnin --submit benself cs345_ec1 fas.zip
