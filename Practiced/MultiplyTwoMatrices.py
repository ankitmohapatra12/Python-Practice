#program to multiply two matrices

l1=[[2,3,3],
    [2,4,6],
    [7,43,5]]
l2=[[2,3,3],
    [2,4,6],
    [7,43,5]]
res=[[0,0,0],
    [0,0,0],
    [0,0,0]]
for i in range(len(l1)):
    for j in range(len(l2[0])):
        for k in range(len(l2)):
            res[i][j]+=l1[i][k]*l2[k][j]
        
for r in res:
    print(r)