# https://www.acmicpc.net/problem/2660
n = int(input())

def floyd_warrshall(graph) :
    for k in range(n) :
        for i in range(n):
            for j in range(n) :
                if graph[i][j] == 0 :
                    graph[i][j] = graph[i][k] + graph[k][j]
            
    return graph

graph = [[0] * n for _ in range(n)]

while True :
    a,b = map(int,input().split())
    if a == -1 and b == -1 :
        break
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1
    
print(graph)
graph = floyd_warrshall(graph)

print(graph)



    
    