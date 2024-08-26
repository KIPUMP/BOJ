# https://www.acmicpc.net/problem/16173
from collections import deque
import sys
input = sys.stdin.readline

dx = [0,1]
dy = [1,0]

def bfs(x,y) :
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True    
    while queue :
        x,y = queue.popleft()
        for i in range(2) :
            nx = x + (dx[i] * arr[x][y])
            ny = y + (dy[i] * arr[x][y])
            
            if 0 <= nx < n and 0 <= ny < n :
                if not visited[nx][ny] : 
                    visited[nx][ny] = True
                    queue.append((nx,ny))


n = int(input())        # 한 변의 길이
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

bfs(0,0)

if visited[n-1][n-1] :
    print("HaruHaru")
else :
    print("Hing")




# 34072	60

