from collections import deque
N, M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(x,y) :
  queue = deque()
  queue.append((x,y))

  while queue :
    x,y = queue.popleft()

    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= N or ny < 0 or ny >= M :
        continue

      if arr[nx][ny] == 0 :
        continue

      if arr[nx][ny] == 1 :
        arr[nx][ny] = arr[x][y] + 1
        queue.append((nx , ny))

  return arr[N-1][M-1]

print(bfs(0,0))



