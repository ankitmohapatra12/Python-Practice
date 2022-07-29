year = int(input("Enter year :"))
if(year%4==0):
    print(year,"is a leap year")
elif(year%400==0):
    print(year,"is a leap year")
elif(year%100==0):
    print(year,"is a not leap year")
else:
    print(year,"is a not leap year")