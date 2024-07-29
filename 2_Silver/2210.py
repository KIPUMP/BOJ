# https://www.acmicpc.net/problem/2210
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

r,c = map(int,input().split())
arr = [list(input().rstrip()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]


dx = [0,1,0,-1]
dy = [1,0,-1,0]

total_sheep = 0
total_wolves = 0

def predation(sheep,wolves) :                   # 울타리 안 늑대와 양 계산
    global total_sheep , total_wolves
    if sheep <= wolves :
        total_wolves += wolves
    else :
        total_sheep += sheep


def dfs(x,y) :                                  # 깊이 우선 탐색
    global sheep, wolves
    visited[x][y] = True                        # 방문 처리
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c :
            if not visited[nx][ny] :
                visited[nx][ny] = True          # 방문 처리
                if arr[nx][ny] != '#' :
                    if arr[nx][ny] == 'v' :     # 늑대 수 count
                        wolves += 1             
                    elif arr[nx][ny] == 'k' :
                        sheep += 1              # 양 수 count
                    dfs(nx,ny)


for i in range(r) :
    for j in range(c) :
        if arr[i][j] == 'v' and not visited[i][j]:
            wolves = 1
            sheep = 0
            dfs(i,j)
            predation(sheep,wolves)
                
        elif arr[i][j] == 'k' and not visited[i][j] :
            sheep = 1
            wolves = 0
            dfs(i,j)
            predation(sheep,wolves)
                            
            
print(total_sheep,total_wolves)

#	31772	108