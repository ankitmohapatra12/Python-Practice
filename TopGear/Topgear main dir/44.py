
l = [10,20,15,40,13]
b = 5
sum_list=[]
def sum(l,b,sum_list):
    sum_list = list(map(lambda x: x + b,l))
    return list(sum_list)


def sub(l,b,sum_list):
    sum_list = list(map(lambda x: x - b,l))
    return list(sum_list)



def mul(l,b,sum_list):
    sum_list = list(map(lambda x: x + b,l))
    return list(sum_list)


def div(l,b,sum_list):
    sum_list = list(map(lambda x: x / b,l))
    return list(sum_list)


def mod(l,b,sum_list):
    sum_list = list(map(lambda x: x % b,l))
    return list(sum_list)


def floor_div(l,b,sum_list):
    sum_list = list(map(lambda x: x // b,l))
    return list(sum_list)



print(sum(l,b,sum_list))
print(sub(l,b,sum_list))
print(mul(l,b,sum_list))
print(div(l,b,sum_list))
print(mod(l,b,sum_list))
print(floor_div(l,b,sum_list))