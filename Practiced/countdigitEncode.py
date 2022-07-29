l1 = input().split()
st = l1[0]
print(l1)
l2=  list(st)
num = l1[1]
ctr=0
for i in l2:
    if i == num:
        ctr+=1
        
print(ctr)