import os


print("Training data with Nivreeager Algorithm: ")
os.system("java -jar -Xmx5000m -Xms5000m ../maltparser-1.9.2/maltparser-1.9.2.jar -c nivreagereg -i ../en-universal-train.conll -m learn -a nivreeager");
os.system("java -jar -Xmx5000m -Xms5000m ../maltparser-1.9.2/maltparser-1.9.2.jar -c nivreagereg -i ../en-universal-dev.conll -o dev.out.ex.2.nivreeager.conll -m parse");

print("Performance of Nivreeager: ")
os.system("perl ../conll-eval.pl -g dev.out.ex.1.a.40000.conll -s dev.out.ex.1.a.40000.conll -q")

print("Training data with stackeager: ")

os.system("java -jar -Xmx5000m -Xms5000m ../maltparser-1.9.2/maltparser-1.9.2.jar -c stackeagereg -i ../en-universal-train.conll -m learn -a stackeager");
os.system("java -jar -Xmx5000m -Xms5000m ../maltparser-1.9.2/maltparser-1.9.2.jar -c stackeagereg -i ../en-universal-dev.conll -o dev.out.ex.2.stackeager.conll -m parse");


print("Training data with stacklazy: ")

os.system("java -jar -Xmx5000m -Xms5000m ../maltparser-1.9.2/maltparser-1.9.2.jar -c stacklazyeg -i ../en-universal-train.conll -m learn -a stacklazy");
os.system("java -jar -Xmx5000m -Xms5000m ../maltparser-1.9.2/maltparser-1.9.2.jar -c stacklazyeg -i ../en-universal-dev.conll -o dev.out.ex.2.stacklazy.conll -m parse");