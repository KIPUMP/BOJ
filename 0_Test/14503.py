import sys
from collections import deque

input = sys.stdin.readline

# 북, 동, 남, 서 방향 (0, 1, 2, 3)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left(direction):
    return (direction - 1) % 4

def bfs(x, y, direction):
    # 현재 위치 청소
    visited[x][y] = True
    result = 1

    while True:
        found_new_place = False
        # 왼쪽 방향으로 회전하며 탐색
        for _ in range(4):
            direction = turn_left(direction)
            nx = x + dx[direction]
            ny = y + dy[direction]

            # 왼쪽 방향에 청소되지 않은 공간이 있다면 이동
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 0:
                visited[nx][ny] = True
                x, y = nx, ny
                result += 1
                found_new_place = True
                break

        # 네 방향 모두 청소되었거나 벽인 경우
        if not found_new_place:
            # 현재 방향에서 뒤로 후진 (현재 방향의 반대 방향으로 이동)
            back_direction = (direction + 2) % 4
            nx = x + dx[back_direction]
            ny = y + dy[back_direction]

            # 후진할 수 있으면 후진
            if arr[nx][ny] == 0:
                x, y = nx, ny
            else:
                # 후진할 수 없으면 작동을 멈춤
                break

    return result

# 입력 처리
n, m = map(int, input().split())
x, y, direction = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# 청소된 공간의 수 출력
print(bfs(x, y, direction))
