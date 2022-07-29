#print the least frequent string
str1 = input("enter string :")
empty ={}
for i in str1:
    if i in empty:
        empty[i]+=1
    else:
        empty[i]=1
p = min(empty,key=empty.get)
print(str(p))
        