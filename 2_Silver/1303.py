from collections import deque

n,m = map(int,input().split())
arr = [list(input().rstrip()) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
queue = deque()

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs_W(x,y) :
  global w_cnt
  queue.append((x,y))
  visited[x][y] = True
  while queue :
    x,y = queue.popleft()
    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < m and 0 <= ny < n :
        if visited[nx][ny] == False and arr[nx][ny] == 'W' :
          w_cnt += 1
          queue.append((nx,ny))
          visited[nx][ny] = True
        

def bfs_B(x,y) :
  global b_cnt
  queue.append((x,y))
  visited[x][y] = True
  while queue :
    x,y = queue.popleft()
    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < m and 0 <= ny < n :
        if visited[nx][ny] == False and arr[nx][ny] == 'B' :
          b_cnt += 1
          queue.append((nx,ny))
          visited[nx][ny] = True
        
total_w = 0
total_b = 0

for i in range(m) :
  for j in range(n) :
    if visited[i][j] == False :
      if arr[i][j] == 'W' :
        w_cnt = 1
        bfs_W(i,j)
        total_w += w_cnt ** 2

      if arr[i][j] == 'B' :
        b_cnt = 1
        bfs_B(i,j)
        total_b += b_cnt ** 2

print(total_w,total_b)