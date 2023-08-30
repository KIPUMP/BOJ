from collections import deque
import sys
sys.setrecursionlimit(10**6)
N = int(input())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
graph = [list(map(int,input())) for _ in range(N)]
def dfs(a,b) :
  if a < 0 or a >= N or b < 0 or b >= N :
    return False 
  
  if graph[a][b] == 1 :
    global count 
    count += 1
    graph[a][b] = 0
    for i in range(4) :
      nx = a + dx[i] 
      ny = b + dy[i]
      dfs(nx,ny)
    return True
  return False 

count = 0
result = 0
cnt =[]
for i in range(N) :
  for j in range(N) :
    if dfs(i,j) == True :
      cnt.append(count)
      result += 1
      count = 0

cnt.sort()
print(result)
for i in range(len(cnt)) :
  print(cnt[i])
