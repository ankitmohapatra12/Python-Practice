def check1(m1,m2):
    for i in range(rows):
        for j in range(cols):
            if(m1[i][j]!=m2[i][j]):
                return 0
    return 1

rows = int(input())
cols = int(input())

m1 =[]
m2= []
for i in range(rows):
    a=[]
    for j in range(cols):
        
        a.append(int(input()))
        print(end=" ")
    print()
    m1.append(a)
for i in range(rows):
    c=[]
    for j in range(cols):
        c.append(int(input()))
    print()
    m2.append(c)

for i in range(rows):
    for j in range(cols):
        print(m1[i][j],end=" ")
    print("")

if(check1(m1,m2)==1):
    print("matrix 1 and matrix 2 are identical ")
else:
    print("not identical ")

    
