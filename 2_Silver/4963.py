import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
dx = [0,1,0,-1,1,-1,1,-1]
dy = [1,0,-1,0,1,-1,-1,1]

def dfs(x,y) :
  visited[x][y] = True
  for i in range(8) :
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < h and 0 <= ny < w :
      if world[nx][ny] == 1 and visited[nx][ny] == False:
        dfs(nx,ny)

while True:
  w,h = map(int,input().split())
  if w == 0 and h == 0 :
    break
  world = [list(map(int,input().split())) for _ in range(h)]
  visited = [[False] * w for _ in range(h)]
  cnt = 0
  for i in range(h) :
    for j in range(w) :
      if world[i][j] == 1 and visited[i][j] == False:
        dfs(i,j)
        cnt += 1
  print(cnt)


