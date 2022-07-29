import math
import sys


def sum_f(a,b):
    return int(a + b)

def sub(a,b):
    if a >= b:
        return a - b
    else:
        return b - a


def mul(a,b):
    return a * b


def div(a,b):
    if a >= b:
        return a / b
    else:
        return b / a

def square_root(a):
    return int(math.sqrt(a))

def floor_div(a,b):
    if a >= b:
        return a // b
    else:
        return b // a


def modulo(a , b):
    return a % b


def prime_check(a):
    ct=0
    for i in range(1,a+1):
        if(a % i == 0):
            ct+=1
        else:
            continue
    if ct <= 2 :
        return "Prime !"
    else:
        return "Non-prime !"



def check_fibonacci(n):
    index = 0
    l = []
    for i in range(0, n):

        if len(l) <= 1:
            l.append(i)

        else:

            l.append(l[index + 1] + l[index])
            index += 1

    return l











import calc as c

print("Addition  5,5:",c.sum_f(5,5))
print("Substraction 5,8:",c.sub(5,8))
print("Multiplication 5,10:",c.mul(5,10))
print("division 10,5:",c.div(10,5))
print("floor check 11,6:",c.floor_div(11,6))
print("Modulo   10,3:",c.modulo(10,3))
print("Squareroot 100:",c.square_root(100))
print("Fibonacci  10:",c.check_fibonacci(10))
print("Prime Check 7:",c.prime_check(7))

