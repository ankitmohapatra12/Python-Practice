#program to print the number of matching characters in two given string
import re
string1 = input("Enter 1st string :")
string2 = input("enter 2nd String :")
s1 = list(string1)
s2 = list(string2)
ctr=0
for ch in s1:
    if re.search(ch,string2):
        ctr=ctr+1
print(ctr)