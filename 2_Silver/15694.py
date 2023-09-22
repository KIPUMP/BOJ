from itertools import permutations

N,M = map(int,input().split())
arr = list(map(int,input().split()))
result = []
for i in permutations(arr,M) :
    result.append(i)
    
result.sort()

for i in result :
    print(*i)