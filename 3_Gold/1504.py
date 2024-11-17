import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    distance = [float('inf')] * n
    pq = []
    distance[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > distance[current_node]:
            continue

        for next_node, weight in arr[current_node]:
            dist = current_dist + weight
            if dist < distance[next_node]:
                distance[next_node] = dist
                heapq.heappush(pq, (dist, next_node))

    return distance

n, e = map(int, input().split())
arr = [[] for _ in range(n)]

for _ in range(e):
    a, b, c = map(int, input().split())
    arr[a-1].append((b-1, c))
    arr[b-1].append((a-1, c))

v1, v2 = map(int, input().split())
v1, v2 = v1-1, v2-1  # 0-based index로 변환

# 각 출발점에서의 최단 거리 계산
shortest_path = dijkstra(0)
move_to_v1 = dijkstra(v1)
move_to_v2 = dijkstra(v2)

# 두 경로 계산
path_1 = shortest_path[v1] + move_to_v1[v2] + move_to_v2[n-1]
path_2 = shortest_path[v2] + move_to_v2[v1] + move_to_v1[n-1]

# 두 경로의 비교
result = min(path_1, path_2)

if result >= float('inf'):
    print(-1)
else:
    print(result)

    
# 64280	360