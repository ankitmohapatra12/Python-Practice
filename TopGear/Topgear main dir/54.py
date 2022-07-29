try:
    x = input("Enter :")
    print("Checking for keyboardInterupt !")
except KeyboardInterrupt:
    print("Exception in keyboard interupt occured !")
else:
    print("No Exceptions occured")




try:
    f = input("Enter  :")
    print(a)
except NameError:
    print("Name Err ->",NameError)

else:
    print("No error !")





try:
    val = int(input("Enter number :"))
    q = val/0
    print(q)
except ArithmeticError:
    print("Arithmetic Error occured",ArithmeticError)

else:
    print("No error !")

finally:
    print("End !!")

