from collections import deque

n,m = map(int,input().split())
track = [list(map(int,input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
queue = deque()

dx = [0,1]
dy = [1,0]

def bfs(x,y) :
    global cnt
    queue.append((x,y))
    while queue :
        x,y = queue.popleft()
        for i in range(2) :
            for j in range(track[x][y] + 1) :
                nx = x + dx[i] * j
                ny = y + dy[i] * j
                if 0 <= nx < n and 0 <= ny < m :
                    if visited[nx][ny] == 0 :
                        queue.append((nx,ny))
                        visited[nx][ny] = visited[x][y] + 1
bfs(0,0)
print(visited[-1][-1]-1)

                    

    
    
