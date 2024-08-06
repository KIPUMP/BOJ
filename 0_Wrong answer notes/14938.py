# https://www.acmicpc.net/problem/14938
import sys
input = sys.stdin.readline

def floyd_warshall() :                  # 모든 경로의 수색 가능 거리 수색 (플로이드 워셜)
    for k in range(n) :
        for i in range(n) :
            for j in range(n) :
                if graph[i][k] + graph[k][j] <= m :
                    graph[i][j] = min(graph[i][j] , graph[i][k] + graph[k][j])
                    

n,m,r = map(int,input().split())  # 지역, 수색범위, 길의 개수

graph = [[1e9] * n for _ in range(n)]
items = list(map(int,input().split()))  # 각 구역의 아이템의 수

for _ in range(r) :                     # 양방향 그래프 삽입
    a,b,l = map(int,input().split())
    
    graph[a-1][b-1] = l
    graph[b-1][a-1] = l
    
for i in range(n) :                     # 자기노드 0 초기화
    graph[i][i] = 0 
    
floyd_warshall()

result = []

for i in range(n) :
    cnt = 0
    for j in range(n) :
        if graph[i][j] <= m :           # 수색범위보다 작으면 아이템 추가       
            cnt += items[j]
            
    result.append(cnt)
    
print(max(result))
            
# 31120	120