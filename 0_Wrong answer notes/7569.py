from collections import deque
m,n,h = map(int,input().split())
box = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
queue = deque()
visited = [[[False] * m for _ in range(n)] for _ in range(h)]
def bfs() :
  dz = [1,0,-1,0,0,0]
  dy = [0,1,0,-1,0,0]
  dx = [0,0,0,0,1,-1]
  while queue :
    x,y,z = queue.popleft()
    for i in range(6) :
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]

      if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
        if box[nx][ny][nz] == 0 and visited[nx][ny][nz] == False :
          box[nx][ny][nz] = box[x][y][z] + 1
          visited[nx][ny][nz] = True
          queue.append((nx,ny,nz))

for i in range(h) :
  for j in range(n) :
    for k in range(m) :
      if box[i][j][k] == 1 and visited[i][j][k] == False :
        queue.append((i,j,k))

bfs()

for i in range(h) :
  for j in range(n) :
    for k in range(m) :
      if box[i][j][k] == 0:
        print(-1)
        exit(0)

max_val = max(box[0][0])

for i in range(h):
  for j in range(n) :
    if max_val < max(box[i][j]) :
      max_val = max(box[i][j])

print(max_val-1)