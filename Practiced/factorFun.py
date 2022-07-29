l1=eval(input("Enter  :"))
j=0
i=1
for j in l1:
    for i in l1:
        if l1[i]%l1[j]==0:
            print(l1[i])
            