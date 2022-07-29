
try:
    x = input("Enter :")
    print("Checking for keyboardInterupt !")
except KeyboardInterrupt:
    print("Exception in keyboard interupt occured !")
else:
    print("No Exceptions occured")