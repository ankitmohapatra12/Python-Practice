str = input()
n =len(str)
l1 = list(str)
l2=[]
print(l1)

dic = dict((i,l1.count(i)) for i  in l1)
print(dic)

for i in dic:
    if dic[i]>1:
        l2.append(i)
        
print(len(l2))