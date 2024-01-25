from itertools import combinations

n,m,k = map(int,input().split())
result = 0
all = [*combinations([i for i in range(n)],m)]

for i in all :
  cnt = 0
  for j in range(m) :
    if i[j] < m :
      cnt += 1
  if cnt >= k :
    result += 1

print(result / len(all))