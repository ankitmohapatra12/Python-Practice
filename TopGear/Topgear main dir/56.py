
a=0
try:
    f = open("E:\python programs\data_1044.txt","r")
    print(f.read())
except IOError as e:
    a=1
    print("Exception occured as :",e)
else:
    print("No exception generated")



finally:



    if a != 1:
        f.close()
        print("File closed !!!! ")





import math as m
i=-10
try:
    print(m.sqrt(i))

except ValueError as ve:
    print(ValueError,"Exception occured as ->   ",ve)
else:
    print("No exception")