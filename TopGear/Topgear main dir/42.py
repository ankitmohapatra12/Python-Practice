# 42
# Functions: Write
# a
# program
# to
# generate
# a
# Fibonacci
# series
# using
# a
# function
# called
# fib(n),
# a) Where ‘n’ is user
# specified
# argument
# specifies
# number
# of
# elements in the
# series.
#
#     sol():
n = int(input("Enter :"))
l = []


def fib(n):
    index = 0
    for i in range(0, n):

        if len(l) <= 1:
            l.append(i)

        else:

            l.append(l[index + 1] + l[index])
            index += 1

    print(l)


fib(n)

