# 41.Dictionary  and Date & Time	Using calendar module perform following operations.
# a) Print the 2016 calendar with space between months as 10 characters.
# b) How many leap days between the years 1980 to 2025.
# c) Check given year is leap year or not.
# d) print calendar of any specified month of the year 2016.


# sol(a) ->

import calendar as c

year =  2016

for i in range(1,12):
    print((c.month(year,i)))
    print("                 ")



#
# sol(b) :
r1 = 1980
r2 = 2025

leap_days_count=0

for i in range(r1,r2+1) :

    if (i%400 ==0) or (i%4==0) :
        leap_days_count+=1
    else :
        continue


print(leap_days_count)





# sol(c):

year = 1996



if (year%400 ==0) or (year%4==0) :
    print(year,"is a leap year")
else :
    print(year,"is a not leap year")




# sol(d) :
import calendar as c

year =  2016

month = input()
dic = {}
for i in range(1,13):
    dic[c.month_name[i]] = i


print(c.month(year,dic[month]))
