toy = list(map(int, input().split()))
print(toy)
ans=sum(toy)
toy.sort()
print(ans-toy[len(toy)-1],ans-toy[0])