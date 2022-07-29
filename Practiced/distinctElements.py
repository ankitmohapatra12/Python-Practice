# l1 = list(map(int,input().strip().split()))
# print(l1)
# l2=[]
# for i in l1:
#     if i not in l2:
#         l2.append(i)
#             
#             
# print(l1)
# print(l2)
#

def unique(l1):
    l1set = set(l1)
    l1list = list(l1set)
    print(l1list)
        
        
l1 = list(map(int,input().strip().split()))
unique(l1)