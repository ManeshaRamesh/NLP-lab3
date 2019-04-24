import os

#To extract teh first few columns
def parse(file_in,file_out ):
	train_file = open(file_in, "r");
	parsed_train_file = open(file_out, "w");
	count = 0;
	for line in train_file:
		list = line.split("\t");
		#print(list);
		if(list[0] == "\n"):
			parsed_train_file.write("\n");
			#print list[0];
		else:
			parsed_train_file.write(list[1]+"\t"+list[3]+"-"+list[4]+"\n");
			#print(list[1]+"\t"+list[3]+"-"+list[4])
		#if count == 3:
	#		break;
		#count= count+1;
	parsed_train_file.close();
	train_file.close();


#To extract just the words
def parse2(file_in, file_out):
	count = 0;
	dev_file = open(file_in, "r");
	parsed_dev_file = open(file_out, "w");
	for line2 in dev_file:
		list2 = line2.split("\t");
		#print(list2);
		if list2[0] == "\n":
			parsed_dev_file.write("\n");
			#print("\n");	
		else:
			parsed_dev_file.write(list2[1] + "\n");
			#print(list2[1]);
		
		#if count == 3:
		#	break;
		#count = count + 1;
	parsed_dev_file.close();
	dev_file.close();



#Default values
print('''
Converting the train and dev files to hunpos...
Extracting the words from the dev file...
''')
parse("../en-universal-train.conll", "en-universal-train.hunpos");
parse("../en-universal-dev.conll", "en-universal-dev.hunpos");
parse2("../en-universal-dev.conll", "en-universal-dev.words");

def run_commands(tag, emission, suff_len, rare_freq):
	print("a) tag-order= "+str(tag)+", emission order = "+str(emission)+",suffix length = "+str(suff_len)+", rare frequency = "+str(rare_freq)+"\n");

	os.system("cat en-universal-train.hunpos | ../hunpos-1.0-macosx/hunpos-train -t"+str(tag)+" -e"+str(emission)+" -s"+str(suff_len)+" -f"+str(rare_freq)+" ex.3.tag3.tagger");
	os.system("cat en-universal-dev.words | ../hunpos-1.0-macosx/hunpos-tag ex.3.tag3.tagger > dev.ex3.tag3.hunpos");
	os.system("perl ../pos-eval.pl en-universal-dev.hunpos dev.ex3.tag3.hunpos");

#print("DIFFERENT TAG VALUESI\n");
#different tag values
run_commands(1,2,10,10);
run_commands(2,2,10,10);
run_commands(3,2,10,10);
run_commands(4,2,10,10);
run_commands(5,2,10,10);

#diffrent emission values
print("DIFFERENT EMISSION VALUES\n");
run_commands(2,1,10,10);
run_commands(2,2,10,10);
run_commands(2,3,10,10);
run_commands(2,4,10,10);
run_commands(2,5,10,10);
print("DIFFERENT SUFFIX LENGTH\n"); 
run_commands(2,2,8,10);
run_commands(2,2,9,10);
run_commands(2,2,10,10);
run_commands(2,2,11,10);
run_commands(2,2,12,10);

print("DIFFERENT RARE FREQUENCY\n");
run_commands(2,2,10,8);
run_commands(2,2,10,9);
run_commands(2,2,10,10);
run_commands(2,2,10,11);
run_commands(2,2,10,12);





