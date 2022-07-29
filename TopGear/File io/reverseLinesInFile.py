f = open("E:\python programs\data_101.txt","r")
str_lst = []
for line in f:
    str_lst.append(line)
[print(x,end="\n") for x in str_lst[::-1]]