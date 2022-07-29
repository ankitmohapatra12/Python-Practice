import math as m
i=-10
try:
    print(m.sqrt(i))

except ValueError as ve:
    print(ValueError,"Exception occured as ->   ",ve)
else:
    print("No exception")
