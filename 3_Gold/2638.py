from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]


dx = [0,-1,0,1]
dy = [-1,0,1,0]

queue = deque()

def bfs() : 
  visited = [[False] * m for _ in range(n)]
  queue.append((0,0))
  visited[0][0] = True
  while queue :
    x,y = queue.popleft()
    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m :
        if not visited[nx][ny] :
          if arr[nx][ny] >= 1 :
            arr[nx][ny] += 1
          else :
            queue.append((nx,ny))
            visited[nx][ny] = True

  
def check_arr() :
  melted = 0
  for i in range(n) :
    for j in range(m) :
      if arr[i][j] >= 3 :
        arr[i][j] = 0
        melted += 1
      elif arr[i][j] >= 2 :
        arr[i][j] = 1

  return melted

time = 0
while True:
    bfs()
    melted = check_arr()
    if melted:
        time += 1
    else: 
        print(time)
        break




