row = int(input())
l=5

for i in range(1,row+1):
    if l!=0:
        s = str(l)
        s1=s+" "
        print(s1*i)
        l=l-1   
