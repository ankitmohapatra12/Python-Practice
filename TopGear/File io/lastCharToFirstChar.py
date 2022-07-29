f = open("E:\python programs\data_101.txt","r")
str = []

res = []
str_line=""

for line in f :
    str.append(line)

for line in str[::-1]:
    str_line+=line[::-1]
    res.append(str_line)


[print(x) for x in res]

