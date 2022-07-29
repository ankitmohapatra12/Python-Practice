# stringop.py
def list_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    print("Sorted:", arr)


def binarySearch(list1, item):
    list1.sort()
    first = 0
    last = len(list1) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) / 2
        if list1[midpoint] == item:
            found = True
            return found
        else:
            if item < list1[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


def list_rev(l):
    print
    l.reverse()
    print("reversed:", l)


# strpackage.py
from stringop import *

list_sort([23, 81, 42, 51, 31])
print("binarySearch([23,81,42,51,31]):",binarySearch([23, 81, 42, 51, 31]))
list_rev([23, 81, 42, 51, 31])



