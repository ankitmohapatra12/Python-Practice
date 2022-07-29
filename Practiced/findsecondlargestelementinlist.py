l1 = [2,3,5,0,5,6,6]
l1.sort()
#print(l1)
i=l1[len(l1)-1]
print(i)
while(i in l1):
    l1.remove(i)
    
j=l1[len(l1)-1]
print(l1)
print(j)