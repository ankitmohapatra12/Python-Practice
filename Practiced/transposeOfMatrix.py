#program to find transpose of matrix
from itertools import chain
l1 = [[2,3,2],
     [22,3,22]
    ,[3,4,6]]
for m in l1:
    print(m)
print()
print()
l = zip(*l1)
for i in l:
    print(i)