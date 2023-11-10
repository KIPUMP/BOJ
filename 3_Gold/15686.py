import sys
from itertools import combinations

input = sys.stdin.readline

n,m = map(int,input().split())
city = [list(map(int,input().split())) for _ in range(n)]
result = 99999

house = []
chicken = []

for i in range(n) :
  for j in range(n) :
    if city[i][j] == 1 :
      house.append([i,j])
    elif city[i][j] == 2 :
      chicken.append([i,j])

for chi in combinations(chicken,m) :
  temp = 0
  for h in house :
    chicken_len = 999
    for j in range(m) :
      chicken_len = min(chicken_len,abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
    temp += chicken_len
  result = min(result,temp)

print(result)