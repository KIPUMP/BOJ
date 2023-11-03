from collections import deque
n,m = map(int,input().split())
arr = [list(map(int,input())) for _ in range(n)]

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
queue = deque()

dx = [0,-1,0,1]
dy = [-1,0,1,0]
visited[0][0][0] = 1 
def bfs(x,y,z) :
  queue.append((x,y,z))
  while queue :
    x,y,z = queue.popleft()
    if x == n-1 and y == m-1 :
      return visited[n-1][m-1][z]
    
    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m :
        if arr[nx][ny] == 0 and visited[nx][ny][z] == 0 :
          visited[nx][ny][z] = visited[x][y][z] + 1
          queue.append((nx,ny,z))
        if arr[nx][ny] == 1 and z == 0 :
          visited[nx][ny][1] = visited[x][y][z] + 1
          queue.append((nx,ny,1))
  return -1

print(bfs(0,0,0))
