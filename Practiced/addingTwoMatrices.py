#python program to add two matrices
l1=[[2,3,4],
    [4,3,2],
    [2,4,3]]
l2=[[2,3,4],
    [4,3,2],
    [2,4,3]]
res=[[0,0,0],
    [0,0,0],
    [0,0,0]]
for i in range(len(l1)):
    for j in range(len(l2)):
        res[i][j]=l1[i][j]+l2[i][j]

for i in res:
    print(i)