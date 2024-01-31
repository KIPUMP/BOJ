# from itertools import combinations
# n,m = map(int,input().split())
# arr = [i for i in range(1,n+1)]

# for i in combinations(arr,m) :
#   print(*i)

import sys
sys.setrecursionlimit(10**6)
n,m = map(int,input().split())
result = []
def dfs(x) :
  if len(result) == m :
    print(*result)
    return

  else :
    for i in range(x,n+1) :
      if i not in result :
        result.append(i)
        dfs(x+1)
        result.pop()

dfs(1)