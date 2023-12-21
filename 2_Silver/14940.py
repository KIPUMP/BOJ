from collections import deque
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
queue = deque()
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(x,y) :
    queue.append((x,y))
    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m :
                if arr[nx][ny] == 1 :
                    arr[nx][ny] = arr[x][y] + 1
                    queue.append((nx,ny))
                    

for i in range(n) :
    for j in range(m) :
        if arr[i][j] == 2 :
            bfs(i,j)
            

for i in range(n) :
    for j in range(m) :
        if arr[i][j] > 0 :
            print(arr[i][j] - 2 ,end = " ")
        else :
            print(arr[i][j], end = " ")
    print()

