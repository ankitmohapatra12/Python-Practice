#program to find the max frequency characters in a string
from collections import Counter
str = input("enter string :")
l = Counter(str)
p=min(l,key=l.get)
print(l)
print(p)