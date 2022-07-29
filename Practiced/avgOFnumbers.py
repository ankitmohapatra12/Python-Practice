




def avg(l1):
    sum=0
    for i in l1:
        sum=sum+i;
    res =  sum//len(l1)
    print(res)
    
n = int(input())
l1=[]
for i in range(n):
    n1 = int(input())
    l1.append(n1)
print(l1)
avg(l1)