# https://www.acmicpc.net/problem/10282
import heapq,sys

input = sys.stdin.readline

def dijkstra(start) :
    distance = [int(1e9)] * n
    distance[start] = 0
    pq = []
    pq.append((0,start))
    visited[start] = True
    
    while pq :
        cur_dist, cur_node = heapq.heappop(pq)
        visited[cur_node] = True
        
        if cur_dist > distance[cur_node] :
            continue
        
        for i in network[cur_node] :
            sum_distance = cur_dist + i[1]
            if sum_distance < distance[i[0]] :
                distance[i[0]] = sum_distance
                heapq.heappush(pq,(sum_distance,i[0]))
                
    return distance
        


for _ in range(int(input())) :              # 테스트 케이스
    n,d,c = map(int,input().split())        # 컴퓨터 개수, 의존성 개수, 컴퓨터 번호
    network = [[] for _ in range(n)]
    visited = [False] * n
    
    for _ in range(d) :
        a,b,s = map(int,input().split())    # 의존 , 감염 시간
        network[b-1].append((a-1,s))
        
    result = dijkstra(c-1)
    max_val = 0
    
    for i in result :
        if max_val < i < int(1e9) :
            max_val = i
    
    print(visited.count(True), max_val)
    
# 48548	656