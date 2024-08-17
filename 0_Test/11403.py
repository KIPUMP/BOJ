# https://www.acmicpc.net/problem/11403

def floyd_warshall(arr) :
    for k in range(n) :
        for i in range(n) :
            for j in range(n) :
                if arr[i][k] == 1 and arr[k][j] == 1 :
                    arr[i][j] = 1
                    
    return arr


n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

graph = floyd_warshall(graph)

for i in range(n) :
    for j in range(n) :
        print(graph[i][j], end=" ")
    print()

# 	31120	96