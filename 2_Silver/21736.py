import sys
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())

school = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
cnt = 0
dx = [0,-1,0,1]
dy = [-1,0,1,0]

def dfs(x,y) :
  global cnt
  visited[x][y] = True
  for i in range(4) :
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < n and 0 <= ny < m :
      if not visited[nx][ny]:
        if school[nx][ny] == 'O' :
          dfs(nx,ny)
        elif school[nx][ny] == 'P' :
          cnt +=1
          dfs(nx,ny)


for i in range(n) :
  for j in range(m) :
    if not visited[i][j] and school[i][j] == 'I' :
      dfs(i,j)

if cnt == 0 :
  print('TT')
else :
  print(cnt)




  