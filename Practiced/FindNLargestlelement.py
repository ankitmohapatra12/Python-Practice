

def func(list1,n):
    final_list=[]
    for i in (0,n):
        max=0
        for j in range(len(list1)):
            if list1[j]>max:
                max=list1[j]
                
        list1.remove(max)
        final_list.append(max)
            
    print(final_list)
    
n = int(input("enter n val : "))
list1 = [2,3,5,232,432,32,0]
func(list1,n)