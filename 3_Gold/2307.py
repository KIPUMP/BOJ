# https://www.acmicpc.net/problem/2307
import sys, heapq

input = sys.stdin.readline

def dijkstra(start,arr,road_num) :
    distance = [int(1e9)] * n
    pq = []
    distance[start] = 0
    heapq.heappush(pq,(0,start))
    
    while pq :
        current_dist, current_node = heapq.heappop(pq)
        if current_dist > distance[current_node] :
            continue
        
        for node,dist,road in arr[current_node] :
            if road != road_num :           # 특정 번호의 길 무시
                total = dist + current_dist
                if total < distance[node] :
                    distance[node] = total
                    heapq.heappush(pq,(total,node))
        
    return distance[n-1]

n,m = map(int,input().split())
arr = [[] for _ in range(n)]
for i in range(m) :
    a,b,t = map(int,input().split())        
    arr[a-1].append((b-1,t,i))          # 길에 특정 번호 부여
    arr[b-1].append((a-1,t,i))
    

shortest_path = dijkstra(0,arr,m)       # 통제 X 일때 최단 거리;

result = []

for i in range(m) :
    x = dijkstra(0,arr,i)               # 각 길(번호)를 통제 했을 때 최단거리
    if x < int(1e9) :                   
        result.append(x-shortest_path)  # 지연시간
        
    else :
        result.append(-1)               # 지연시간이 무한대일때

if min(result) == -1 :
    print(-1) 
    
else :
    print(max(result))

# 164088	4900