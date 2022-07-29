no_of_pounds_float = float(input("Enter total pounds :"))
no_of_pounds = round(no_of_pounds_float,2)


kg = 0.45359237

assert no_of_pounds >= 0,"less that zero"
assert no_of_pounds >100,"less than 100"
print(round(no_of_pounds*kg),2)