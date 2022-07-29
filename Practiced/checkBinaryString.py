#check if a string is binary
import string
str = input("enter string :")
l = list(str)
binary="01"
ctr=0
digit = string.digits
for ch in l:
    if ch in digit and ch in binary or ch==' ':
        ctr=ctr+1
if ctr==len(str):
    print("string is binary.")
else:
    print("string is not binary.")
#print(digit)