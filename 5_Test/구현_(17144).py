import sys
input = sys.stdin.readline

# 미세먼지 확산 방향 (상, 우, 하, 좌)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 미세먼지 확산 함수
def spread_dust(arr):
    new_arr = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j] > 0:
                dust = arr[i][j]
                spread_amount = dust // 5
                spread_count = 0

                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < r and 0 <= ny < c:
                        if arr[nx][ny] != -1:  # 공기청정기 부분은 확산 안됨
                            new_arr[nx][ny] += spread_amount
                            spread_count += 1

                # 확산 후 남은 먼지
                new_arr[i][j] += dust - (spread_amount * spread_count)

    # 공기청정기 위치 유지
    for i in range(r):
        for j in range(c):
            if arr[i][j] == -1:
                new_arr[i][j] = -1
    return new_arr

# 공기청정기 작동 (상단 청정기 x 좌표, 하단 청정기 x 좌표) 
def cleaner(upper, lower):
    # 상단 청정기 (반시계 방향)
    # 아래쪽에서 위로 이동
    for i in range(upper - 1, 0, -1):
        arr[i][0] = arr[i - 1][0]
    # 왼쪽에서 오른쪽으로 이동
    for i in range(c - 1):
        arr[0][i] = arr[0][i + 1]
    # 위쪽에서 아래로 이동
    for i in range(upper):
        arr[i][c - 1] = arr[i + 1][c - 1]
    # 오른쪽에서 왼쪽으로 이동
    for i in range(c - 1, 1, -1):
        arr[upper][i] = arr[upper][i - 1]
    arr[upper][1] = 0  # 청정 후 공기 배출

    # 하단 청정기 (시계 방향)
    # 위쪽에서 아래로 이동
    for i in range(lower + 1, r - 1):
        arr[i][0] = arr[i + 1][0]
    # 왼쪽에서 오른쪽으로 이동
    for i in range(c - 1):
        arr[r - 1][i] = arr[r - 1][i + 1]
    # 아래쪽에서 위로 이동
    for i in range(r - 1, lower, -1):
        arr[i][c - 1] = arr[i - 1][c - 1]
    # 오른쪽에서 왼쪽으로 이동
    for i in range(c - 1, 1, -1):
        arr[lower][i] = arr[lower][i - 1]
    arr[lower][1] = 0  # 청정 후 공기 배출

# 입력 읽기
r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]

# 공기청정기 위치 찾기
air_purifier = []
for i in range(r):
    if arr[i][0] == -1:
        air_purifier.append(i)

upper = air_purifier[0]
lower = air_purifier[1]

# 각 시간 단계별 시뮬레이션
for _ in range(t):
    arr = spread_dust(arr)
    cleaner(upper, lower)

# 남은 먼지 계산
total = sum(sum(row) for row in arr) + 2  # 청정기 위치를 제외하고 계산
print(total)
