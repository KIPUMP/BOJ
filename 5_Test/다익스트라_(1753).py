# https://www.acmicpc.net/problem/1753
import sys, heapq
input = sys.stdin.readline

def dijkstra(graph,start,v) :               # 그래프 , 시작노드, 간선수
    dist = [1e9] * v                        # 최단경로 초기화
    dist[start] = 0
    pq = [(0,start)]                        # 우선 순위 큐(가중치, 시작 노드)

    while pq :
        current_dist, u =  heapq.heappop(pq)    # 노드 u에 연결된 모든 인접 노드(가중치, 연결 노드)들을 검사
        
        if current_dist > dist[u] :
            continue
        
        for weight, v in graph[u] :             # 노드 u에 연결된 모든 인접노드의 가중치 검사
            distance = current_dist + weight
            
            if distance < dist[v] :             # 새로운 최단 경로를 발견하면 dist를 갱신하고 우선순위 큐에 추가 
                dist[v] = distance
                heapq.heappush(pq,(distance,v))
    return dist
                
V,E = map(int,input().split())              # 간선 , 정점
K = int(input())                            # 시작 노드
graph = [[] for _ in range(V)]
for _ in range(E) :
    u,v,w = map(int,input().split())        
    graph[u-1].append((w,v-1))                # 시작노드 - (무게, 간선)
    
dist = dijkstra(graph,K-1,V)

for d in dist :
    if d == 1e9 :
        print("INF")
    else :
        print(d)
        




