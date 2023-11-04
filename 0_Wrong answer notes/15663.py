import sys
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
arr = sorted(map(int,input().split()))
visited = [False] * n
result = []
def dfs() :
  if len(result) == m :
    print(*result)
    return
  else :
    remember = 0
    for i in range(n) :
      if not visited[i] and remember != arr[i] :
        result.append(arr[i])
        visited[i] = True
        remember = arr[i]
        dfs()
        visited[i] = False
        result.pop()

dfs()