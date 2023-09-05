import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
house = [input() for _ in range(N)]
visited = [[False] * M for _ in range(N)]

def dfs(x, y):
    visited[x][y] = True

    if house[x][y] == "-":
        for i in [1, -1]:
            ny = y + i
            if 0 <= ny < M and house[x][ny] == "-" and not visited[x][ny]:
                dfs(x, ny)

    if house[x][y] == "|":
        for i in [1, -1]:
            nx = x + i
            if 0 <= nx < N and house[nx][y] == "|" and not visited[nx][y]:
                dfs(nx, y)

cnt = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j] and (house[i][j] == "-" or house[i][j] == "|"):
            cnt += 1
            dfs(i, j)

print(cnt)
