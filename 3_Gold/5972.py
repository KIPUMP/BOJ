# https://www.acmicpc.net/problem/5972
# 한 지점(1 - 현서) 에서 다른 지점(N-찬홍))의 최단 소요 거리
import sys,heapq
input = sys.stdin.readline

def dijkstra(graph,start) :             # 현서가 찬홍이까지의 최소의 여물을 구하기 위해 다익스트라로 구한다
    distance = [1e9] * n
    distance[start] = 0
    pq = [(0,start)]
    
    while pq :
        current_distance,node = heapq.heappop(pq)
        
        if current_distance > distance[node] :      # 현재 뽑은 길이가 지금까지 최단 거리보다 길면 무시
            continue
        
        for point,dist in graph[node] :
            if dist + current_distance < distance[point] :
                distance[point] = current_distance + dist
                heapq.heappush(pq,(distance[point],point))
        
    return distance

n,m = map(int,input().split())
arr = [[] for _ in range(n)]
for _ in range(m) :
    a,b,c = map(int,input().split())
    arr[a-1].append((b-1,c))
    arr[b-1].append((a-1,c))

arr = dijkstra(arr,0)

print(arr[n-1])

#	51424	208