def neatPrint(results):
	for ii in range(0, len(results)):
		print(results[ii]);
	print;
	
def parseTuple(str, charsToReplace):
	#charsToReplace = ['(',')','\'',','];
	for ii in charsToReplace:
		str = str.replace(ii, '');
	return str.split(' ');
	
def printRow(list,width):
	col = ""
	format = "%-" + str(width) + "s| "
	print "| " + (''.join((format%(col) for col in parseTuple(list,['(',')','\'',',']))))
	
def neatPrintTable(results):
	width = 15
	dashes = "-" * (width - 1);
	top_bot = (" -" + dashes + "-") * (len(results[0]))
	print top_bot
	printRow(str(results[0]), width)
	print "|" + (" " + dashes + " +") * (len(results[0])-1) + " " + dashes + " |"
	for ii in range(1, len(results)):
		printRow(str(results[ii]),width)
	print top_bot
	print "\t" + str(len(results)) + " rows selected";
	