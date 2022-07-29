import calendar as c

year =  2016

month = input()
dic = {}
for i in range(1,13):
    dic[c.month_name[i]] = i


print(c.month(year,dic[month]))




#for i in range(1,12):
   # print((c.month(year,i)))
    #print("                 ")

