import sys
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
board = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

result = 0

dx = [0,-1,0,1] 
dy = [-1,0,1,0]

def dfs(x,y) :
    global result
    visited[x][y] = True
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m :
            if not visited[nx][ny] and board[nx][ny] == '0':
                dfs(nx,ny)
        
        if nx == n-1 :
            result = 1
            
for i in range(m) :
    if not visited[0][i] and board[0][i] == '0':
        dfs(0,i)
        
if result == 1 :
    print("YES")
else :
    print("NO")
                
            
