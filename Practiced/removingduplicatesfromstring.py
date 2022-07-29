#Removing duplicates from string and printing the string
import re
string1 = input("Enter 1st string :")
#l1= list(string1)
empty=""
for ch in string1:
    if ch in empty:
        pass
    else:
        empty=empty+ch
print(empty)
