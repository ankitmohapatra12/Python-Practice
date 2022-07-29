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

