a = int(input("enter num 1 :"))
b = int(input("enter num 2 :"))
c = int(input("enter num 3 :"))
d = int(input("enter num 4 :"))


def find_large(*args):
    max = 0
    for i in args:
        if i > max:
            max = i
        else:
            continue
    return max

large = find_large(a,b,c,d)
print(large)