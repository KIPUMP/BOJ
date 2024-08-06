# https://www.acmicpc.net/problem/1916
# 다익스트라
import sys, heapq
input = sys.stdin.readline

def dijkstra(graph,start) :
    distance = [1e9] * n
    distance[start] = 0
    primary_queue = [(0,start)]     # (시작노드, 거리 삽입)
    
    while primary_queue:
        current_distance,node = heapq.heappop(primary_queue)

        if current_distance > distance[node] :      # 1e9 거르기 
            continue
        
        for v,weight in graph[node] :
            total_distance = current_distance + weight
            if total_distance < distance[v] :
                distance[v] = total_distance
                heapq.heappush(primary_queue,(total_distance,v))
    return distance

n = int(input())
m = int(input())
graph = [[] for _ in range(n)]

for i in range(m) :
    s, e, cost = map(int,input().split())
    graph[s-1].append((e-1,cost))
    
start,end = map(int,input().split())

dist = dijkstra(graph,start-1)

print(dist[end-1])