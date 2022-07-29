f = open("E:\python programs\data_10.txt","w+")


input = '''Python Lambda Functions are anonymous function means that the function is without a name.
As we already know that the def keyword is used to define a normal function in Python.
Similarly, the lambda keyword is used to define an anonymous function in Python. 
Python Lambda Function Syntax:
lambda arguments: expression
 '''


f.write(input)

f1=open("E:\python programs\data_101.txt","r")
str=""
index=0
while 1 :
    char = f1.read(1)
    index+=1
    if not char:
        break
    str = str + char;
    if(len(str)==10):
        print(str)
        str = ""
        print("Index :",index)








f1.close()



file = open("E:\python programs\data_101.txt","r")
str=""
index=0
while(1):
    c = file.read(1)
    index+=1
    str=str+c
    if not c:
        break
    if(index == 100):
        break
    print(c,end="")
file.seek(0)
file.close()



file = open("E:\python programs\data_101.txt","r")
str=""
index=0

for line in file:
    index=index+1
    if index > 4:
        print(line,end="")
    else:
        continue

