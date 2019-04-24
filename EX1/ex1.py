
import os



# extract the first four lines and stores it in "en-universal-train-4.conll"
def text_extract(file_in, file_out, number):
	f_in = open(file_in, "r");
	f_out = open(file_out, "w");
	count = 0

	for line in f_in:
		if count == int(number):
			break;
		f_out.write(line); 
		if (line[0] == "\n"):
			count = count +1;
			

	print(str(count)+ " lines printesd in " + file_out);
	f_out.close();

	f_in.close();

input_filename = "../en-universal-train.conll"
text_extract(input_filename, "en-universal-train-4.conll", 4);
text_extract(input_filename, "en-universal-train-40.conll", 40);
text_extract(input_filename, "en-universal-train-400.conll", 400);
text_extract(input_filename, "en-universal-train-4000.conll", 4000);


#learns and runs the parser. Then it evaluates it

print("FOR 40000 LINES: ");
os.system("java -jar -Xmx5000m -Xms5000m ../maltparser-1.9.2/maltparser-1.9.2.jar -c parser-all -i ../en-universal-train.conll -m learn");
os.system("java -jar -Xmx5000m -Xms5000m ../maltparser-1.9.2/maltparser-1.9.2.jar -c parser-all -i ../en-universal-dev.conll -o dev.out.ex.1.a.40000.conll -m parse");


print("FOR 4000 LINES: ");
os.system("java -jar -Xmx5000m -Xms5000m ../maltparser-1.9.2/maltparser-1.9.2.jar -c parser-all -i en-universal-train-4000.conll -m learn");
os.system("java -jar -Xmx5000m -Xms5000m ../maltparser-1.9.2/maltparser-1.9.2.jar -c parser-all -i ../en-universal-dev.conll -o dev.out.ex.1.a.4000.conll -m parse");

print("FOR 400 LINES: ");
os.system("java -jar -Xmx5000m -Xms5000m ../maltparser-1.9.2/maltparser-1.9.2.jar -c parser-all -i en-universal-train-400.conll -m learn");
os.system("java -jar -Xmx5000m -Xms5000m ../maltparser-1.9.2/maltparser-1.9.2.jar -c parser-all -i ../en-universal-dev.conll -o dev.out.ex.1.a.400.conll -m parse");

print("FOR 40 LINES: ");
os.system("java -jar -Xmx5000m -Xms5000m ../maltparser-1.9.2/maltparser-1.9.2.jar -c parser-all -i en-universal-train-40.conll -m learn");
os.system("java -jar -Xmx5000m -Xms5000m ../maltparser-1.9.2/maltparser-1.9.2.jar -c parser-all -i ../en-universal-dev.conll -o dev.out.ex.1.a.40.conll -m parse");

print("FOR 4 LINES: ");
os.system("java -jar -Xmx5000m -Xms5000m ../maltparser-1.9.2/maltparser-1.9.2.jar -c parser-all -i en-universal-train-4.conll -m learn");
os.system("java -jar -Xmx5000m -Xms5000m ../maltparser-1.9.2/maltparser-1.9.2.jar -c parser-all -i ../en-universal-dev.conll -o dev.out.ex.1.a.4.conll -m parse");


# print("Evaluation 1: \n");

# print("For corpus of 40000 lines")
# os.system("perl ../conll-eval.pl -g dev.out.ex.1.a.40000.conll -s dev.out.ex.1.a.40000.conll -q")

# print("For corpus of 4000 lines")
# os.system("perl ../conll-eval.pl -g dev.out.ex.1.a.40000.conll -s dev.out.ex.1.a.4000.conll -q")

# print("For corpus of 400 lines")
# os.system("perl ../conll-eval.pl -g dev.out.ex.1.a.40000.conll -s dev.out.ex.1.a.400.conll -q")
# print("For corpus of 40 lines")
# os.system("perl ../conll-eval.pl -g dev.out.ex.1.a.40000.conll -s dev.out.ex.1.a.40.conll -q")
# print("For corpus of 4 lines")
# os.system("perl ../conll-eval.pl -g dev.out.ex.1.a.40000.conll -s dev.out.ex.1.a.4.conll -q")


print("Evaluation 2: \n");

print("For corpus of 40000 lines")
os.system("perl ../conll-eval.pl -g ../en-universal-dev.conll -s dev.out.ex.1.a.40000.conll -q")

print("For corpus of 4000 lines")
os.system("perl ../conll-eval.pl -g ../en-universal-dev.conll -s dev.out.ex.1.a.4000.conll -q")

print("For corpus of 400 lines")
os.system("perl ../conll-eval.pl -g ../en-universal-dev.conll -s dev.out.ex.1.a.400.conll -q")
print("For corpus of 40 lines")
os.system("perl ../conll-eval.pl -g ../en-universal-dev.conll -s dev.out.ex.1.a.40.conll -q")
print("For corpus of 4 lines")
os.system("perl ../conll-eval.pl -g ../en-universal-dev.conll -s dev.out.ex.1.a.4.conll -q")