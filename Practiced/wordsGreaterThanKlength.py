#find words which are greater than k length and print those words
str = input("Enter string :")
n = int(input("enter k length :"))
l1 = str.split(" ")
for ch in l1:
    if len(ch)>n:
        print(ch)
        