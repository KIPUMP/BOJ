from collections import deque
import sys
input = sys.stdin.readline

def bfs(x,y) :
    
    # (좌,상,우,하)
    dx = [0,-1,0,1]
    dy = [-1,0,1,0]
    
    queue.append([x,y])                         
    visited[x][y] = True                        # 방문 처리
    
    while queue :
        x,y = queue.popleft()                   
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny  < m :
                if not visited[nx][ny] and arr[nx][ny] == '1':
                    arr[nx][ny] = int(arr[x][y]) + 1
                    visited[nx][ny] = True      # 방문처리
                    queue.append([nx,ny])       
                    
    return arr[n-1][m-1]
        

queue = deque()
n,m = map(int,input().split())
visited = [[False] * m for _ in range(n)]
arr = [list(input().rstrip()) for _ in range(n)]

print(bfs(0,0))

