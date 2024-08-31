# https://www.acmicpc.net/problem/1261
import heapq

dx = [0,-1,0,1]
dy = [-1,0,1,0]

def dijkstra(x,y) :
    distance = [[1e9] * m for _ in range(n)]
    distance[x][y] = 0
    pq = []
    heapq.heappush(pq,(distance[x][y] , x , y))
    
    while pq :
        current_distance, x , y = heapq.heappop(pq)
        
        if current_distance > distance[x][y] :
            continue
        
        for i in range(4) :
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0 <= nx < n and 0 <= ny < m :
                if arr[nx][ny] == '1' :
                
                    break_count = current_distance + 1      # 벽을 부심

                    if distance[nx][ny] > break_count :
                        distance[nx][ny] = break_count
                        heapq.heappush(pq,(distance[nx][ny],nx,ny))

                else :
                    break_count = current_distance
                    if distance[nx][ny] > break_count :
                        distance[nx][ny] = break_count
                        heapq.heappush(pq,(distance[nx][ny],nx,ny))
                    
    return distance
    
    
m,n = map(int,input().split())
arr = [list(input().rstrip()) for _ in range(n)]

result = dijkstra(0,0)

print(result[n-1][m-1])

# 33188	56