


def mul_args1(*args):
    l = input().strip().split()
    list1 = [int(x) for x in l]
    for i in args:
        if i in list1:
            print(i, "is present in ", list1)


mul_args1(3, 1, 5)
