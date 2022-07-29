#to find to uncommon words between 2 strings
str1 = input("Enter string1 :")
str2 = input("Enter string2 :")

list1 =  str1.split()
list2 = str2.split()
uc= ""
for i in list1:
    if i not in list2:
       uc=uc+" "+i
print(uc)