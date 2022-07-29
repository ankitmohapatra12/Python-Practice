r1 = 1980
r2 = 2025

leap_days_count=0

for i in range(r1,r2+1) :
    print(i)
    if (i%400 ==0) or (i%4==0) :
        leap_days_count+=1
    else :
        continue


print(leap_days_count)

