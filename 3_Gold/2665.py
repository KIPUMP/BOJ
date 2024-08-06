# https://www.acmicpc.net/problem/2665
import sys
import heapq

input = sys.stdin.readline

# 격자에서 이동할 방향 (왼쪽, 위, 오른쪽, 아래)
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def dijkstra(graph, x, y):
    # 초기 위치의 거리를 0으로 설정
    distance[0][0] = 0
    pq = [(0, x, y)]  # (비용, x, y)
    
    while pq:
        cnt, x, y = heapq.heappop(pq)
        
        # 현재 비용이 기록된 거리보다 크면 스킵
        if cnt > distance[x][y]:
            continue
        
        # 가능한 4개의 방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                # 벽을 기준으로 새로운 비용 계산
                new_cost = cnt + (1 if graph[nx][ny] == 0 else 0)
                
                # 새로운 비용이 작으면 업데이트하고 큐에 푸시
                if new_cost < distance[nx][ny]:
                    distance[nx][ny] = new_cost
                    heapq.heappush(pq, (new_cost, nx, ny))
    
    return distance[n-1][n-1]

# 입력 받기
n = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(n)]

# 거리 배열을 높은 값으로 초기화
distance = [[1e9] * n for _ in range(n)]

# 최소 변환 횟수 계산
min_conversion_count = dijkstra(arr, 0, 0)
print(min_conversion_count)

# 33188	44