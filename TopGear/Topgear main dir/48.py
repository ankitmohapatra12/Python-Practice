import math as m

a = int(input("Enter num 1 :"))
b = int(input("Enter num 2 :"))


def sum(a,b) :
    return a+b
def sub(a,b) :
    if a>=b :
        return a-b
    else:
        return b-a
def mul(a,b) :
    return a*b

def div(a,b) :
    if a >= b:
        return a / b
    else:
        return b / a


def find_square_root(*args):
    l=[]
    for i in args:
        l.append(m.sqrt(i))
    print(l)


def split_string(sample_str,ch):
    string_list = sample_str.strip().split(ch+" ")
    print(string_list)


print(sum(a,b))
print(sub(a,b))
print(mul(a,b))
print(div(a,b))



find_square_root(36,69,81)



sample_str = "Pack: My: Box: With: Good: Food"
ch=':'
split_string(sample_str,ch)
