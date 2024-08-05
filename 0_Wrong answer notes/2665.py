# https://www.acmicpc.net/problem/2665
import sys , heapq
input = sys.stdin.readline

dx = [0,-1,0,1]
dy = [-1,0,1,0]

def dijkstra(graph,start) :
    



n = int(input())
graph = [[] for _ in range(n)]
for i in range(n-1) :
    arr = list(input().rstrip())
    for j in range(n) :
        if arr[i][j] == arr[i+1][j]:
            graph[i].append((i+1,1))
            graph[i+1].append((i,1))
            
visited = [[False] * n for _ in range(n)]



