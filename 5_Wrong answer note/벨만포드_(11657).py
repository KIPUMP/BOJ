# https://www.acmicpc.net/problem/11657
import sys
input = sys.stdin.readline

def bellman_ford(graph,start) :
    distance = [1e9] * (n)
    distance[start] = 0                 # 초기 노드 0 
    
    for i in range(n-1) :
        for start,end,weight in graph :
            if distance[start] != 1e9 and distance[start] + weight < distance[end] :
                distance[end] = distance[start] + weight
        
    for i in range(n-1) :
        for start, end, weight in graph : 
            if distance[start] != 1e9 and distance[start] + weight < distance[end] :
                return -1
    
    return distance
n,m = map(int,input().split())
graph = []
for _ in range(m) :
    a,b,c = map(int,input().split())
    graph.append((a-1,b-1,c))
    
dist = bellman_ford(graph,0)

if dist == -1 :
    print(-1)
else :
    for i in dist[1:] :
        if i == 1e9 :
            print(-1)
        else :
            print(i)
        
        