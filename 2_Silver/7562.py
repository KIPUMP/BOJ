# https://www.acmicpc.net/problem/7562
from collections import deque
import sys
input = sys.stdin.readline
# 나이트가 움직일 수 있는 좌표 정의
dx = [-2,2,-1,1,1,-1,-2,2]      
dy = [-1,1,-2,2,-2,2,1,-1]

def bfs(x,y) :
    queue.append([x,y])
    visited[x][y] = True
    while queue :
        x,y = queue.popleft()
        for i in range(8) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l :
                if not visited[nx][ny] :
                    arr[nx][ny] = arr[x][y] + 1
                    visited[nx][ny] = True
                    queue.append([nx,ny])
                    


for _ in range(int(input())) :                  # 테스트 케이스
    l = int(input())                            # 한변의 길이
    x1,y1 = map(int,input().split())              
    x2,y2 = map(int,input().split())
    queue = deque()
    
    visited = [[False] * l for _ in range(l)]
    arr = [[0] * l for _ in range(l)]
    
    arr[x2][y2] = 1                             # end point 1로 초기화
    
    if x1 == x2 and y1 == y2 :                  # 좌표가 같으면 bfs 탐색 X
        print(0)
    else :
        bfs(x1,y1)
        print(arr[x2][y2])

    
# 34072	2472
    