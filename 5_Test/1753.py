import sys, heapq
input = sys.stdin.readline

def dijkstra(graph,start) :
  distance = [1e9] * (V)
  distance[start] = 0
  pq = [(0,start)]              # 무조건 (가중치, 노드) 우선순위 큐
  
  while pq :
      dist,node = heapq.heappop(pq)     
      
      if dist > distance[node] :
            continue
          
      for n, weight in graph[node] :
            total_distance = dist + weight
            
            if total_distance < distance[n] :
                  distance[n] = total_distance
                  heapq.heappush(pq,(total_distance,n))
  return distance

V,E = map(int,input().split())
K = int(input())
arr = [[] for _ in range(V)]

for _ in range(E) :
  u,v,w = map(int,input().split())
  arr[u-1].append((v-1,w))
              
dist = dijkstra(arr,K-1)

for i in dist :
  if i == 1e9 :
    print("INF")
  else :
    print(i)