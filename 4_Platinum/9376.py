from collections import deque

queue = deque()
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(x,y) :
    global cnt,result
    queue.append((x,y))
    visited[x][y] = True
    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w :
                if not visited[nx][ny] :
                    if jail[nx][ny] == '#' :
                        jail[nx][ny] = '.'
                        cnt += 1
                        result.append(cnt)
                        visited[nx][ny] = True
                        
                    if jail[nx][ny] == '.' :
                        visited[nx][ny] = True
                        queue.append((nx,ny))
                    
        
    
for _ in range(int(input())) :
    h,w = map(int,input().split())
    jail = [list(input().rstrip()) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    result = []
    cnt = 0
    for i in range(h) :
        for j in range(w) :
            if jail[i][j] == '$' and not visited[i][j] :
                bfs(i,j)
                
    print(cnt)
    
    
    

    