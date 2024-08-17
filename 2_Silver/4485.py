# https://www.acmicpc.net/problem/4485
# 특정 노드에서 출발하는 최소값 출력 → 다익스트라 
import sys, heapq                   # 다익스트라 알고리즘 pq 사용
input = sys.stdin.readline

dx = [0,-1,0,1]
dy = [-1,0,1,0]

def dijkstra(x,y) :
    distance = [[1e9] * n for _ in range(n)]
    distance[x][y] = graph[x][y]
    pq = [(x,y)]
    
    while pq :
        x,y= heapq.heappop(pq)
        
        if distance[x][y] < graph[x][y] :
            continue
        
        for i in range(4) :
            nx = dx[i] + x 
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n :
                if distance[x][y] + graph[nx][ny] < distance[nx][ny] :
                    distance[nx][ny] = distance[x][y] + graph[nx][ny]
                    heapq.heappush(pq,(nx,ny))
            
            
    return distance[n-1][n-1]
        
    
    


t = 0                   # 테스트 케이스 수
while True :
    t += 1
    n = int(input())
    if n == 0 :
        break
    graph = [list(map(int,input().split())) for _ in range(n)]
    print(f"Problem {t}: {dijkstra(0,0)}")
    
    
# 33188	376