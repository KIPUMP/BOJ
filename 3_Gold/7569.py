from collections import deque
import sys
input = sys.stdin.readline
m,n,h = map(int,input().split())
box = []
for _ in range(h) :
    box.append([list(map(int,input().split())) for _ in range(n)])

dy = [0,1,0,-1,0,0]
dz = [1,0,-1,0,0,0]
dx = [0,0,0,0,1,-1]

queue = deque([])

visited = [[[False] * m for _ in range(n)] for _ in range(h)]

def bfs() :
    while queue :
        x,y,z = queue.popleft()
        for i in range(6) :
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
                if box[nx][ny][nz] == 0 and visited[nx][ny][nz] == False:
                    box[nx][ny][nz] = box[x][y][z] + 1
                    queue.append([nx,ny,nz])
                    visited[nx][ny][nz] = True
             

for i in range(h) :
    for j in range(n) :
        for k in range(m) :
            if box[i][j][k] == 1 and visited[i][j][k] == False:
                visited[i][j][k] = True
                queue.append([i,j,k])

bfs()

answer = 0
for a in box:
    for b in a:
        for c in b:
            if c == 0:
                print(-1)
                exit(0)            
        answer = max(answer, max(b))

print(answer-1)