# https://www.acmicpc.net/problem/2665
import sys 
from collections import deque

input = sys.stdin.readline

dx = [0,-1,0,1]
dy = [-1,0,1,0]

def bfs() :
    queue = deque()
    queue.append((0,0))
    visited[0][0] = 0
    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n :
                if arr[nx][ny] == 1 :
                    if visited[nx][ny] > visited[x][y] :
                        visited[nx][ny] = visited[x][y]
                        queue.appendleft((nx,ny))

                else :
                    if visited[nx][ny] > visited[x][y] + 1:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx,ny))


    return visited[n-1][n-1]

n = int(input())
arr = [list(map(int,input().rstrip())) for _ in range(n)]
visited = [[1e9] *n for _ in range(n)]

print(bfs())

# 34220	56




