n=int(input("enter total list size :"))
list1 = list(map(int,input("enter element :").strip().split()))[:n]
s1 = set()
print(list1)
for i in list1:
    for j in list1:
        if(i == j):
            s1.add(i)
l1 = list(s1)  
print(l1)  