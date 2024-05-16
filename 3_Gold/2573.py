import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and arr[nx][ny] == 0:
                arr[x][y] -= 1
            if not visited[nx][ny] and arr[nx][ny] > 0:
                dfs(nx, ny)

result = 0

while True:
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j] > 0:
                cnt += 1
                dfs(i, j)
    
    if cnt == 0:
        result = 0
        break
    if cnt > 1:
        break
    
    result += 1

print(result)
