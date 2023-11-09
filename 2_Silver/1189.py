import sys
sys.setrecursionlimit(10**6)

r,c,k = map(int,input().split())
board = [list(input()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
cnt = 0

def dfs(x,y,distance) :
  global cnt
  if distance == k and x == 0 and y == c-1 :
    cnt += 1
  else : 
    visited[x][y] = True
    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < r and 0<= ny < c :
        if not visited[nx][ny] and board[nx][ny] == '.' :
          visited[nx][ny] = True
          dfs(nx,ny,distance+1)
          visited[nx][ny] = False

dfs(r-1,0,1)
print(cnt)





