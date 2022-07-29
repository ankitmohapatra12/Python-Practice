from collections import Counter
list1 = [2,3,4,5,3,2,2,4,5,3,4,3,5,5,5,5,2]
list1.sort()
print("unsorted list",str(list1))

result = sorted(list1,key = list1.count,reverse=True)
print("sorted list",str(result))