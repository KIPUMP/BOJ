# https://www.acmicpc.net/problem/2458
import sys
input = sys.stdin.readline

def floyd_warshall(graph) :
    for k in range(n) :
        for i in range(n) :
            for j in range(n) :
                if graph[i][k] and graph[k][j] :
                    graph[i][j] = True
    return graph

n,m = map(int,input().split())
arr = [[False] * n for _ in range(n)]

for i in range(m) :
    a,b = map(int,input().split())
    arr[a-1][b-1] = True

arr = floyd_warshall(arr)

result = 0

for i in range(n) :
    count = 0
    for j in range(n) :
        if arr[i][j] or arr[j][i] :
            count +=1
    
    if count == n - 1 :
        result += 1

print(result)

#	32436	4432