from itertools import product

n,m = map(int,input().split())
arr = sorted(map(int,input().split()))
result = []
for i in product(arr,repeat = m) :
  result.append(i)

result = sorted(set(result))

for i in result :
  print(*i)