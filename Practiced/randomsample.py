import random
num = random.randrange(1,100,2)
print(num)
ctr=0
if num!=0:
    for i in range(2,num):
        if num%i==0:
            ctr=ctr+1
        else:
            pass
    if ctr==1:
        print(num,"is prime.")
    else:
        print(num,"is not prime.")

