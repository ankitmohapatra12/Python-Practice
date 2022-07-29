n = input()
l1 = list(map(int,input().strip().split()))
l2=[]

l3=[]
for i in l1 :
    if i%2==0:
        l2.append(i)
    if i%2==1 and i!=0:
        l3.append(i)

l2.extend(l3)
for i in l2:
    print(i,end=" ")
        