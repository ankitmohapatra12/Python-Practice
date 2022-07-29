n=int(input("enter total :"))
l1=list(map(int,input("enter the element:").strip().split()))[:n]
print(l1)
for i in l1:
    ctr=0
    
    for j in l1:
        if(i == j):
            ctr=ctr+1
    print(i," occured ",ctr," times.")
