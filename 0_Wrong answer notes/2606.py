# https://www.acmicpc.net/problem/2606
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

cnt = 0

def dfs(x) :
    global cnt
    visited[x] = True
    for i in graph[x] :
        if not visited[i] :
            cnt += 1
            dfs(i)
    
n = int(input())                                    # 컴퓨터 대수

graph = [[] for _ in range(n+1)]                    # 그래프 정의 

for _ in range(int(input())) :                      # 네트워크 수 만큼 입력
    a,b = map(int,input().split())                  
    # 노드 양방향 그래프 연결
    graph[a].append(b)             
    graph[b].append(a)

visited = [False] * (n+1)
dfs(1)

print(cnt)
    
    
# 	31120	40

    