# https://www.acmicpc.net/problem/2458
import sys
input = sys.stdin.readline

def floyd_warshall(graph) :
    for k in range(n) :
        for i in range(n) :
            for j in range(n) :
                if arr[i][j] == 0 :
                    graph[i][j] =graph[i][k]+graph[k][j]
                    
                
                
    return graph

n,m = map(int,input().split())
arr = [[0] *n for _ in range(n)]

for _ in range(m) :
    a,b = map(int,input().split())
    arr[a-1][b-1] = 1
    
arr = floyd_warshall(arr)

print(arr)