import sys
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

result = []
picture_len = 0

def dfs(x,y) :
  global picture_len
  visited[x][y] = True
  for i in range(4) :
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < m :
      if not visited[nx][ny] and arr[nx][ny] == 1 :
        picture_len += 1
        visited[nx][ny] = True
        dfs(nx,ny)


for i in range(n) :
  for j in range(m) :
    if arr[i][j] == 1 and not visited[i][j] :
      picture_len += 1
      dfs(i,j)
      result.append(picture_len)

    picture_len = 0


print(len(result))
if len(result) == 0 :
  print(0)
else :
  print(max(result))

      
