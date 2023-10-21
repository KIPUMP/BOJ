import sys
sys.setrecursionlimit(10**6)
N = int(input())

area = []
abnormal_area = [[0] * N for _ in range(N)]

visited = [[False] * N for _ in range(N)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

cnt = 0
cnt_abnormal= 0

for _ in range(N) :
  area.append(input())

for i in range(N) :
  for j in range(N) :
    if area[i][j] == 'B' :
      abnormal_area[i][j] = 1
  

def dfs(x,y) :
  visited[x][y]=True
  
  for i in range(4) :
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < N and 0 <= ny < N :
        if visited[nx][ny] == False :
          if area[x][y] == area[nx][ny]:
            dfs(nx,ny)

def dfs_abnormal(x,y) :
  visited[x][y]=True
  
  for i in range(4) :
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < N and 0 <= ny < N :
        if visited[nx][ny] == False :
          if abnormal_area[x][y] == abnormal_area[nx][ny]:
            dfs_abnormal(nx,ny)

for i in range(N) :
  for j in range(N) :
    if visited[i][j] == False :
      cnt += 1
      dfs(i,j)

visited = [[False] * N for _ in range(N)]

for i in range(N) :
  for j in range(N) :
    if not visited[i][j]:
      cnt_abnormal += 1
      dfs_abnormal(i,j)

print(cnt,cnt_abnormal)