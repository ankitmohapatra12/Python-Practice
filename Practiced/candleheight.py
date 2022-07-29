candles = list(map(int,input().rstrip().split()))
max=0
print(candles)
for i in candles:
    if i>max:
        max=i
print(candles.count(max))
    
    