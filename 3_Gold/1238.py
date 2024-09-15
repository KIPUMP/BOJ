# https://www.acmicpc.net/problem/1238
import sys, heapq
input = sys.stdin.readline

def dijkstra(start) :
    distance = [1e9] *n
    distance[start] = 0
    pq = []
    heapq.heappush(pq,(distance[start],start))
    
    while pq :
        current_distance, now = heapq.heappop(pq)
        
        if current_distance > distance[now] :
            continue
        
        for node, weight in arr[now] :
            dist = current_distance + weight
            if dist < distance[node] :
                distance[node] = dist
                heapq.heappush(pq,(distance[node],node))
    return distance

n,m,x = map(int,input().split())
arr = [[] for _ in range(n)]
for _ in range(m) :
    start,end,weight = map(int,input().split())
    arr[start-1].append((end-1,weight))
    
min_distance = []

for i in range(n) :
    min_distance.append(dijkstra(i))
    
result = []
for i in range(n) :
    result.append(min_distance[i][x-1] + min_distance[x-1][i])
    
print(max(result))

# 72116	840