list1=[2,3,4,56,6,5]
n = len(list1)
list1[0],list1[n-1] = list1[n-1],list1[0]
print(list1)
list1.clear()
print(list1)