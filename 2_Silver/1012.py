import sys
sys.setrecursionlimit(10**6)

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dfs(x,y) :
  for i in range(4) :
    nx = x + dx[i]
    ny = y + dy[i]

    if (0 <= nx < N) and (0 <= ny < M) :
      if arr[nx][ny] == 1 :
        arr[nx][ny] = -1
        dfs(nx,ny)

T = int(input())
for _ in range(T) :
  M,N,K = map(int,input().split())
  arr = [[0] * M for _ in range(N)]
  cnt = 0

  for _ in range(K) :
    m,n = map(int,input().split())
    arr[n][m] = 1 
  
  for i in range(N) :
    for j in range(M) :
      if arr[i][j] > 0 :
        dfs(i,j)
        cnt += 1
  print(cnt)


