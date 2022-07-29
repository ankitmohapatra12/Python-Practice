n = int(input("Enter :"))
l = []



def fib(n):
    index=0
    for i in range(0,n):
        
        if len(l)<=1:
            l.append(i)
          
        else:

            l.append(l[index+1]+l[index])
            index += 1



    print(l)

fib(n)
