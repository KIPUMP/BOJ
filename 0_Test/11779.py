# https://www.acmicpc.net/problem/11779
import sys, heapq

def dijkstra(start, end):
    distance = [int(1e9)] * n
    distance[start] = 0
    prev_node = [-1] * n  # 경로 추적용 리스트
    pq = []
    heapq.heappush(pq, (0, start))
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_distance > distance[current_node]:
            continue
        
        for next_node, weight in arr[current_node]:
            dist = current_distance + weight
            
            if distance[next_node] > dist:
                distance[next_node] = dist
                prev_node[next_node] = current_node
                heapq.heappush(pq, (dist, next_node))
    
    # 최단 경로 추적
    path = []
    current = end
    while current != -1:
        path.append(current + 1)
        current = prev_node[current]
    path.reverse()
    
    return distance[end], path

n = int(input())
m = int(input())

arr = [[] for _ in range(n)]
for _ in range(m):
    start, end, cost = map(int, input().split())
    arr[start - 1].append((end - 1, cost))
    
start, end = map(int, input().split())
result_cost, result_path = dijkstra(start - 1, end - 1)

print(result_cost)
print(len(result_path))
print(" ".join(map(str, result_path)))
