from collections import deque

dx = [0,-1,0,1]
dy = [-1,0,1,0]

n , m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
result = []

def bfs() :
  visited = [[False] * m for _ in range(n)]
  queue = deque()
  queue.append((0,0))
  visited[0][0] = True
  cnt = 0
  while queue :
    x,y = queue.popleft()
    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m :
        if not visited[nx][ny] :
          if arr[nx][ny] == 0:
            visited[nx][ny] = True
            queue.append((nx,ny))
          elif arr[nx][ny] == 1 :
            arr[nx][ny] = 0 
            visited[nx][ny] = True
            cnt += 1
  result.append(cnt)
  return cnt

time = 0

while True :
  time += 1
  cnt = bfs()
  if cnt == 0 :
    break

print(time - 1)
print(result[-2])

      
  


    