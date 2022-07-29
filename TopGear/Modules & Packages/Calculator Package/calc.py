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


