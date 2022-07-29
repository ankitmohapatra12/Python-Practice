f = open("E:\python programs\data_10.txt","w+")
input = '''Python Lambda Functions are anonymous function means that the function is without a name.
As we already know that the def keyword is used to define a normal function in Python.
Similarly, the lambda keyword is used to define an anonymous function in Python. 
Python Lambda Function Syntax:
lambda arguments: expression
This function can have any number of arguments but only one expression, which is evaluated and returned.
One is free to use lambda functions wherever function objects are required.
You need to keep in your knowledge that lambda functions are syntactically restricted to a single expression.
It has various uses in particular fields of programming besides other types of expressions in functions.
Let’s look at this example and try to understand the difference between a normal def defined function and lambda function. 
This is a program that returns the cube of a given value:  '''


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