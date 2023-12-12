# from itertools import combinations 

# while True :
#   lotto = list(map(int,input().split()))
#   n = lotto[0]
#   lotto = sorted(lotto[1:])

#   if n == 0 :
#     break

#   for i in combinations(lotto,6)  :
#     print(*i)

#   print()

import sys
sys.setrecurionlimit(10**6)

def dfs(depth, idx) :
  if depth == 6 :
    print(*out)
    return

  else :
    for i in range(idx,k) :
      out.append(s[i])
      dfs(depth + 1, i + 1)
      out.pop()

while True :
  lotto = list(map(int,input().split()))
  k = lotto[0]
  s = lotto[1:]
  out = []
  dfs(0,0)
  if k == 0 :
    break
  print()