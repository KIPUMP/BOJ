from collections import deque
import sys
input = sys.stdin.readline

# 빙산 배열의 크기 (행, 열)
n, m = map(int, input().split())

# 빙산 배열 입력
arr = [list(map(int, input().split())) for _ in range(n)]

# 방문 여부를 기록하는 배열
visited = [[False] * m for _ in range(n)]

# 상, 하, 좌, 우 방향 벡터
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

# BFS(너비 우선 탐색) 함수 정의
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny]:
                    if arr[nx][ny] == 0:
                        if arr[x][y] > 0:
                            arr[x][y] -= 1
                    else:
                        visited[nx][ny] = True
                        queue.append((nx, ny))

# 결과(년 수)를 초기화
result = 0

while True:
    # 매년마다 방문 배열을 초기화
    visited = [[False] * m for _ in range(n)]
    cnt = 0  # 빙산 덩어리 수
    
    # 빙산 배열을 탐색
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0 and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    
    # 빙산이 두 개 이상의 덩어리로 나뉘었는지 확인
    if cnt >= 2:
        print(result)
        break
    
    # 모든 빙산이 녹았는지 확인
    if cnt == 0:
        print(0)
        break

    # 년 수 증가
    result += 1
