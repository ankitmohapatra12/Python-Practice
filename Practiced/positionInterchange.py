s = input("enter string :")
l1 = list(s)
str=""
n=len(l1);
for i in range(n-1):
    if i%2==0 and i==0:
        str=str+l1[i+1]+l1[i]
        i=i+3
    else:
        str=str+l1[i+1]+l1[i]
        i=i+3
print(str)
#naikt