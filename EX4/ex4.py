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
        #               break;
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
                #       break;
                #count = count + 1;
        parsed_dev_file.close();
        dev_file.close();

#to convert from hunpos to conll format
#To extract just the words
def parse3(file_in, file_out):
        count = 1;
        dev_file = open(file_in, "r");
        parsed_dev_file = open(file_out, "w");
        for line in dev_file:
                list = line.split("\t");
                #print(list);
                if list[0] == "\n":
                        parsed_dev_file.write("\n");
                        #print("\n");
			count = 1;
                else:
                        tags = list[1].split("-");
			#parsed_dev_file.write(str(count) +"\t"+list[0]+"\t_\t"+tags[0]+"\t"+tags[1]+"\t_\t_\t_\t_\t_"+"\n");
			parsed_dev_file.write(str(count) +"\t"+list[0]+"\t_\t"+tags[0]+"\t"+tags[1]+"\t"+"\n");
			#print(tags);
                        #print(str(count) +"\t"+list[0]+"\t-\t"+tags[0]+"\t"+tags[1]);
			count = count+1;
        parsed_dev_file.close();
        dev_file.close();

#Default values
print('''
a) Default values:
 Where tag-order=2, emission order = 2,suffix length = 10, rare frequency = 10
''');
parse("../en-universal-train.conll", "en-universal-train.hunpos");
parse("../en-universal-dev.conll", "en-universal-dev.hunpos");
parse2("../en-universal-dev.conll", "en-universal-dev.words");

def run_commands(tag, emission, suff_len, rare_freq):
        print(" tag-order= "+str(tag)+", emission order = "+str(emission)+",suffix length = "+str(suff_len)+", rare frequency = "+str(rare_freq)+"\n");

        os.system("cat en-universal-train.hunpos | ../hunpos-1.0-macosx/hunpos-train -t"+str(tag)+" -e"+str(emission)+" -s"+str(suff_len)+" -f"+str(rare_freq)+" ex.4.tagger");
        os.system("cat en-universal-dev.words | ../hunpos-1.0-macosx/hunpos-tag ex.4.tagger > dev.ex4.hunpos");
        #os.system("perl ../pos-eval.pl en-universal-dev.hunpos dev.ex4.hunpos");


run_commands(2,4,10,10);
parse3("dev.ex4.hunpos", "dev.ex4.conll");
os.system("cat dev.ex4.conll");
os.system("java -jar -Xmx5000m -Xms5000m ../maltparser-1.9.2/maltparser-1.9.2.jar -c stackprojeg -i ../en-universal-train.conll -m learn -a stackproj");
os.system("java -jar -Xmx5000m -Xms5000m ../maltparser-1.9.2/maltparser-1.9.2.jar -c stackprojeg -i ../en-universal-dev.conll -o dev.ex4.conll -m parse");
os.system("perl ../conll-eval.pl -g ../en-universal-dev.conll -s dev.ex4.conll -q");







