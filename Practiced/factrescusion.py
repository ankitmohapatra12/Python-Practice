def show(num):
    if num==1:
        return fact
    fact=1
    fact=fact*num
    return fact*show(num-1)
num=7
print(show(num))