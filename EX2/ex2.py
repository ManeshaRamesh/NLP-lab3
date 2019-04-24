import os


print("Training data with Nivrestandard Algorithm: ")

os.system("java -jar -Xmx5000m -Xms5000m ../maltparser-1.9.2/maltparser-1.9.2.jar -c nivrestandardconfig -i ../en-universal-train.conll -m learn -a nivrestandard");
# os.system("java -jar -Xmx5000m -Xms5000m ../maltparser-1.9.2/maltparser-1.9.2.jar -c nivrestandardconfig -m info")
os.system("java -jar -Xmx5000m -Xms5000m ../maltparser-1.9.2/maltparser-1.9.2.jar -c nivrestandardconfig -i ../en-universal-dev.conll -o dev.out.ex.2.nivrestandard.conll -m parse");

print("Training data with Stackeager: ")

os.system("java -jar -Xmx5000m -Xms5000m ../maltparser-1.9.2/maltparser-1.9.2.jar -c stackeagerconfig -i ../en-universal-train.conll -m learn -a stackeager");
# os.system("java -jar -Xmx5000m -Xms5000m ../maltparser-1.9.2/maltparser-1.9.2.jar -c stackeagerconfig -m info")

os.system("java -jar -Xmx5000m -Xms5000m ../maltparser-1.9.2/maltparser-1.9.2.jar -c stackeagerconfig -i ../en-universal-dev.conll -o dev.out.ex.2.stackeager.conll -m parse");



# print("Training data with Stacklazy: ")

os.system("java -jar -Xmx5000m -Xms5000m ../maltparser-1.9.2/maltparser-1.9.2.jar -c stacklazyconfig -i ../en-universal-train.conll -m learn -a stacklazy");
# os.system("java -jar -Xmx5000m -Xms5000m ../maltparser-1.9.2/maltparser-1.9.2.jar -c stacklazyeg -m info")

os.system("java -jar -Xmx5000m -Xms5000m ../maltparser-1.9.2/maltparser-1.9.2.jar -c stacklazyconfig -i ../en-universal-dev.conll -o dev.out.ex.2.stacklazy.conll -m parse");

# print("Training data with Stackproj: ")

os.system("java -jar -Xmx5000m -Xms5000m ../maltparser-1.9.2/maltparser-1.9.2.jar -c stackprojconfig -i ../en-universal-train.conll -m learn -a stackproj");
# os.system("java -jar -Xmx5000m -Xms5000m ../maltparser-1.9.2/maltparser-1.9.2.jar -c stacklazyeg -m info")

os.system("java -jar -Xmx5000m -Xms5000m ../maltparser-1.9.2/maltparser-1.9.2.jar -c stackprojconfig -i ../en-universal-dev.conll -o dev.out.ex.2.stackproj.conll -m parse");

# Evalulation gold standard en-universal 

print("Performance of Nivrestandard: ")
os.system("perl ../conll-eval.pl -g ../en-universal-dev.conll -s dev.out.ex.2.nivrestandard.conll -q")

print("Performance of Stackeager: ")
os.system("perl ../conll-eval.pl -g ../en-universal-dev.conll -s dev.out.ex.2.stackeager.conll -q")

print("Performance of Stacklazy: ")
os.system("perl ../conll-eval.pl -g ../en-universal-dev.conll -s dev.out.ex.2.stacklazy.conll -q")

print("Performance of Stackproj: ")
os.system("perl ../conll-eval.pl -g ../en-universal-dev.conll -s dev.out.ex.2.stackproj.conll -q")