str =input("enter string :")
l1=list(str.split(" "))
str1=""
for ele in l1[::-1]:
    print(ele,end=" ")
    