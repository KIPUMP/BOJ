from itertools import combinations

# 입력 값을 받습니다
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []


for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append((i, j))        # 집 좌표 저장
        elif arr[i][j] == 2:        
            chicken.append((i, j))      # 치킨집 좌표 저장

result = 1e9

for chi in combinations(chicken, m):        # m개의 치킨집 조합을 모두 확인합니다
    total_distance = 0
    for hx, hy in house:                    # 현재 조합에 대한 총 치킨 거리 계산
        min_distance = 1e9                  
        for cx, cy in chi:
            distance = abs(hx - cx) + abs(hy - cy)
            min_distance = min(min_distance, distance)
        total_distance += min_distance
    
    result = min(result, total_distance)    # 도시의 치킨거리 최솟값

print(result)
