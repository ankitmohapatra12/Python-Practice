#check if string contains any special characters
import string
#import ascii
str =input("enter a string :")
l1 = list(str)
res = string.ascii_letters+string.digits
print(res)
for ch in l1:
    if ch not in res:
        print(ch,end=" ")