#program for matrix product
from itertools import chain
def dun(val):
    pro=1
    for i in val:
        pro*=i
    return pro
    
    
l1 = [[2,3,2],[3,4,2],[4,4,2,1]]

res = dun(list(chain(*l1)))
print(res)