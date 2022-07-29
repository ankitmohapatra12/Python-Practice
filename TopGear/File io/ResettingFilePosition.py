file = open("E:\python programs\data_101.txt","r")
str=""
index=0
while(1):
    c = file.read(1)
    index+=1
    str=str+c
    if not c:
        break
    if(index == 100):
        break
    print(c,end="")
file.seek(0)
file.close()