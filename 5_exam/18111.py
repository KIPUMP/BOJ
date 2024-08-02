# https://www.acmicpc.net/problem/18111
import sys
input = sys.stdin.readline
n,m,b = map(int,input().split())
ground = [list(map(int,input().split())) for _ in range(n)]

time = int(1e9)
result = 0

# 모든 가능한 높이 (0 ~ 256) 에 대해 조사
for i in range(257):
    use_block = 0  # 블록을 쌓는 데 필요한 블록 수
    take_block = 0  # 블록을 제거하여 얻을 수 있는 블록 수

    # 각 지점의 블록 높이를 확인
    for x in range(n):
        for y in range(m):
            # 현재 높이보다 블록이 높은 경우, 블록을 제거 (take)
            if ground[x][y] > i:
                take_block += ground[x][y] - i
            # 현재 높이보다 블록이 낮은 경우, 블록을 쌓음 (use)
            else:
                use_block += i - ground[x][y]

    # 인벤토리 블록을 사용하여 블록을 쌓을 수 있는지 확인
    if use_block > take_block + b:
        continue  # 블록이 부족한 경우 이 높이는 불가능하므로 다음 높이로 넘어감
    
    # 필요한 총 시간 계산 (블록 제거 시간은 2초, 블록 쌓기 시간은 1초)
    count = take_block * 2 + use_block

    # 현재 높이에서 걸리는 시간이 최소 시간보다 적거나 같은 경우, 업데이트
    if count <= time:
        time = count
        result = i

print(time,result)