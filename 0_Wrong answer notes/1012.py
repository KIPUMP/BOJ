import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
for _ in range(int(input())) :
  m,n,k = map(int,input().split())
  arr = [[0] * m for _ in range(n)]
  def dfs(x,y) :
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
        arr[nx][ny] = 0
        dfs(nx,ny)
        

  for _ in range(k) :
    x,y = map(int,input().split())
    arr[y][x] = 1

  cnt = 0

  for i in range(n) :
    for j in range(m) :
      if arr[i][j] == 1 :
        cnt += 1
        dfs(i,j)
  print(cnt)




