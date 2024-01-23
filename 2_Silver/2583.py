import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m,k = map(int,input().split())
square = [list(map(int,input().split())) for _ in range(k)]

arr = [[0] * (n) for _ in range(m)]
visited = [[False] * n for _ in range(m)]

for i in range(k) :
  for j in range(square[i][0], square[i][2]):
    for k in range(square[i][1],square[i][3]) :
      arr[j][k] = 1

dx = [0,-1,0,1]
dy = [-1,0,1,0]

def dfs(x,y) :
  global area
  visited[x][y] = True
  for i in range(4) :
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < m and 0 <= ny < n :
      if not visited[nx][ny] and arr[nx][ny] == 0 :
        visited[nx][ny] = True
        area += 1
        dfs(nx,ny)

cnt = 0
result = []
for i in range(m) :
  for j in range(n) :
    if arr[i][j] == 0 and not visited[i][j] :
      cnt += 1
      area = 1
      dfs(i,j)
      result.append(area)
      
result.sort()
print(cnt)
print(*result)
