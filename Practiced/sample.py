n = int(input())
l=n-1
j=1
str="#"
for i in range(n):
    print(" "*l+str*j)
    l-=1
    j+=1
    