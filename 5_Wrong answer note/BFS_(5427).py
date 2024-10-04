# https://www.acmicpc.net/problem/5427
from collections import deque
import sys
input = sys.stdin.readline

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def bfs_fire(fire_positions, w, h):
    fire_visited = [[-1] * w for _ in range(h)]
    queue = deque(fire_positions)
    
    for x, y in fire_positions:
        fire_visited[x][y] = 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == '.' and fire_visited[nx][ny] == -1:
                fire_visited[nx][ny] = fire_visited[x][y] + 1
                queue.append((nx, ny))
    
    return fire_visited

def bfs_human(start_x, start_y, fire_visited, w, h):
    human_visited = [[-1] * w for _ in range(h)]
    queue = deque([(start_x, start_y)])
    human_visited[start_x][start_y] = 0
    
    while queue:
        x, y = queue.popleft()
        
        if x == 0 or x == h - 1 or y == 0 or y == w - 1:  # 가장자리에 도달하면 탈출
            return human_visited[x][y] + 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < h and 0 <= ny < w:
                if arr[nx][ny] == '.' and human_visited[nx][ny] == -1:
                    if fire_visited[nx][ny] == -1 or human_visited[x][y] + 1 < fire_visited[nx][ny]:
                        human_visited[nx][ny] = human_visited[x][y] + 1
                        queue.append((nx, ny))
    
    return -1  # 탈출 불가능한 경우

for _ in range(int(input())):
    w, h = map(int, input().split())
    arr = [list(input().strip()) for _ in range(h)]
    
    fire_positions = []
    start_x, start_y = -1, -1
    
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '*':
                fire_positions.append((i, j))
            elif arr[i][j] == '@':
                start_x, start_y = i, j
    
    # 불의 BFS 실행
    fire_visited = bfs_fire(fire_positions, w, h)
    
    # 사람의 BFS 실행
    result = bfs_human(start_x, start_y, fire_visited, w, h)
    
    if result == -1:
        print("IMPOSSIBLE")
    else:
        print(result)

# 115640	2228