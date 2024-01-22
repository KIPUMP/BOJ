import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
sour = []
bitter = []

for _ in range(n) :
  a,b = map(int,input().split())
  sour.append(a)
  bitter.append(b)

diff = float('inf')

for i in range(1,n+1) :
  idxs = list(combinations(list(range(n)),i))

  for food in idxs :
    s = 1
    b = 0

    for j in range(i) :
      s *= sour[food[j]]
      b += bitter[food[j]]

    if abs(s-b) < diff :
      diff = abs(s-b)
      
print(diff)


