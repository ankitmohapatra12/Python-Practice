file = open("E:\python programs\data_101.txt","r")
str=""
index=0

for line in file:
    index=index+1
    if index > 4:
        print(line,end="")
    else:
        continue


