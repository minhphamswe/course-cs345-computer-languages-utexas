FormatDTraceProfile.class: FormatDTraceProfile.java
	javac *java
	jar cmf mainClass FormatDTraceProfile.jar *class
	jar tf FormatDTraceProfile.jar

FormatDTraceProfile.java: FormatDTraceProfile.jj 
	javacc FormatDTraceProfile.jj

clean:
	rm *.class FormatDTraceProfile.java FormatDTraceProfileConstants.java FormatDTraceProfileTokenManager.java ParseException.java SimpleCharStream.java Token.java TokenMgrError.java

submit:
	turnin --submit benself CS345_HW3 HW3.scm Parser.jj FormatDTraceProfile.jj

