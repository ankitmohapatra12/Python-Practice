n = int(input())
l1 = list(map(int,input().strip().split()))
print(l1)
i,j=0,1
arr =[]
sum=0
while(i!=j and i<n+1 and j<n):
    num1 = l1[i]
    num2 = l1[j]
    
    if(num2-num1) > 0:
        arr.append(num2-num1)
        
    else:
        arr.append(num1-num2)
    i+=1
    j+=1
print(arr)
for i in arr:
    sum=sum+i
print(sum)