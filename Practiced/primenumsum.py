#sum of prime number between a given range
r1 =int(input("enter range1 :"))
r2 =int(input("enter range2 :"))
l1 =[]
Sum=0

for r1 in range(r1,r2+1):
    ctr =0
    i=1
    for i in range(i,r1):
        if(r1%i==0 and r1!=0):
            ctr=ctr+1;
        if(r1==1):
            continue;
    if(ctr==1):
        l1.append(r1)
print(l1)
Sum=sum(l1)
print(Sum)