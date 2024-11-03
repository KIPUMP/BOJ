# https://www.acmicpc.net/problem/16946
import sys
from collections import deque, defaultdict
input = sys.stdin.readline

# 방향 배열: 좌, 상, 우, 하
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

# BFS 함수: 연결된 0 영역을 탐색하고 크기를 반환
def bfs(x, y, idx):
    queue = deque([(x, y)])
    visited[x][y] = idx  # 영역 인덱스를 방문 배열에 기록
    count = 1  # 현재 영역의 크기

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and arr[nx][ny] == '0':
                    visited[nx][ny] = idx
                    queue.append((nx, ny))
                    count += 1
    return count

# 입력 받기
n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]  # 방문 배열 생성

# 영역 크기 저장용 사전 및 인덱스
component_size = {}
component_idx = 1

# 0 영역을 탐색하여 크기를 계산하고 저장
for i in range(n):
    for j in range(m):
        if arr[i][j] == '0' and visited[i][j] == 0:
            size = bfs(i, j, component_idx)
            component_size[component_idx] = size
            component_idx += 1

# 결과 배열 생성
result = [[0] * m for _ in range(n)]

# 벽을 부쉈을 때 이동 가능한 영역 크기 계산
for i in range(n):
    for j in range(m):
        if arr[i][j] == '1':
            adjacent_components = set()
            for k in range(4):
                ni, nj = i + dx[k], j + dy[k]
                if 0 <= ni < n and 0 <= nj < m:
                    if visited[ni][nj] > 0:
                        adjacent_components.add(visited[ni][nj])
            # 인접한 영역 크기를 합산하고 벽의 위치 추가, 10으로 나눈 나머지 계산
            wall_count = 1 + sum(component_size[idx] for idx in adjacent_components)
            result[i][j] = wall_count % 10
        else:
            result[i][j] = 0

# 결과 출력
for row in result:
    print("".join(map(str, row)))

# 58696	2112