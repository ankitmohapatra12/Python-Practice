from collections import Counter
str1 = input("enter string :")

res=Counter(str1)
print(res)
p = max(res,key=res.get)
print(str(p))
