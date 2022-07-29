str = input("enter string :")
l1 = str.split(" ")
for ele in l1:
    
    if len(ele)%2==0:
        print(ele,end=" ")
        