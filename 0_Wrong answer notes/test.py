# heap 구조 사용, graph 초기화
# 출발 노드 확인
# 최단 경로 리스트 초기화
# 방문하지 않은 노드 중에서 최단 거리가 짧은 노드 선택
# 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 갱신 반복
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [1e9] * (n+1)

for i in range(m) :
  a,b,c = map(int,input().split())
  graph[a].append((b,c))

def dijkstra(start) :
  distance[start] = 0
  visited[start] = True
  for i in graph[start] :
    distance[i[0]] = i[1]
  
  for i in range(n-1) :
    min_val = 1e9
    idx = 0
    for j in range(1,n+1) :
      if distance[j] < min_val and not visited[j] :
        min_val = distance[j]
        idx = j
      visited[idx] =  True
      for k in graph[idx] :
        cost = distance[idx] + k[1]
        if cost < distance[k[0]] :
          distance[k[0]] = cost


dijkstra(start)

for i in range(1,n+1) :
  if distance[i] == 1e9 :
    print("INF")
  else :
    print(distance[i])


