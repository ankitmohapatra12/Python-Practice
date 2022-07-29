l1=list(map(int,input("Enter:").strip().split(' ')))
emp=[]
for i in range(1,len(l1)):
    emp.append(l1[i]-l1[i-1])
print(max(emp))
    