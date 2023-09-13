from collections import deque

N,M = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(M)]
dx = [0, 1, 0, -1]
dy = [1, 0 ,-1 ,0]
cnt = 0
queue = deque()

for i in range(M):
    for j in range(N):
        if box[i][j] == 1:
            queue.append([i, j])

def bfs():
  while queue:
      x,y = queue.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and box[nx][ny] == 0 :
          queue.append([nx,ny])
          box[nx][ny] += box[x][y] + 1      # 최단 거리
bfs()
for i in box :
  for j in i :
    if j == 0 :
      print(-1)
      exit()
  cnt = max(cnt,max(i))

print(cnt-1)