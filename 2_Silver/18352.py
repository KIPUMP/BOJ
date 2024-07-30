# https://www.acmicpc.net/problem/18352
import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

result = []
def bfs(x) :
    queue.append(x)
    visited[x] = True
    while queue :
        x = queue.popleft()
        for i in graph[x] :             
            if not visited[i] :
                queue.append(i)
                visited[i] = True
                distance[i] = distance[x] + 1
                if distance[i] == k :           # 길이가 k면 결과 배열에 삽입
                    result.append(i)
                
# 도시의 개수(n) , 도로의 개수(m), 거리 정보(k), 출발 도시 (x)
n,m,k,x = map(int,input().split())          
graph = [[] for _ in range(n+1)]            
visited = [False] * (n+1)                   # 방문 처리
distance = [0] * (n+1)                      # 최단 거리 
for i in range(m) : 
    a,b = map(int,input().split())
    graph[a].append(b)                      # 단방향 그래프
    
queue = deque()
bfs(x)
result.sort()                               

if len(result) == 0:
    print(-1)
else :
    for i in result :
        print(i)

	# 101120	1844
    
        
    