import math as m
i=-10
a=0
try:
    xa = input("Enter :")
    print("Checking for keyboardInterupt !")
    x = input("Enter  :")
    print(a)
    val = int(input("Enter number :"))
    q = val / 0
    print(q)
    f = open("E:\python programs\data_1044.txt", "r")
    print(f.read())
    print(m.sqrt(i))
except KeyboardInterrupt:
    print("Exception in keyboard interupt occured !")
except NameError:
    print("Name Err ->",NameError)
except ArithmeticError:
    print("Arithmetic Error occured",ArithmeticError)
except IOError as e:
    a=1
    print("Exception occured as :",e)
except ValueError as ve:
    print(ValueError,"Exception occured as ->   ",ve)
else:
    print("No exception")

finally:
    if a != 1:
        f.close()
        print("File closed !!!! ")