sysDictFile = open("/usr/share/dict/words", "r")
  
outputFile = open("dict.py", "w")

outputFile.write("dict = [")

flag = False

for word in sysDictFile.readlines():
	word = word.strip('\n')
	if flag:
		outputFile.write(',');
	else:
		flag = True
	outputFile.write("\"" + word + "\"")

outputFile.write("]")