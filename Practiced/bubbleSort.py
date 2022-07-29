def bsrt(l1):
    n = len(l1)
    for i in range(n):
        for j in range(0,n-i-1):
            if l1[j] > l1[j+1]:
                l1[j],l1[j+1] = l1[j+1],l1[j]
    s2 = set(l1)
    print(sorted(s2,reverse=True))
                
l1 = list(map(int,input().strip().split()))
print(l1)
bsrt(l1)