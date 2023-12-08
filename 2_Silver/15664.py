import sys
sys.setrecursionlimit(10**6)

n , m = map(int,input().split())
arr = sorted(map(int,input().split()))
visited = [False] * n
result = []

def dfs(start) :
  if len(result) == m:
    print(*result)
    return 

  else :
    remember = ''
    for i in range(start,n) :
      if not visited[i] and remember != arr[i] :
        result.append(arr[i])
        visited[i] = True
        remember = arr[i]
        dfs(i+1)
        result.pop()
        visited[i] = False

dfs(0)


