# https://www.acmicpc.net/problem/2660
n = int(input())

def floyd_warrshall(graph) :
    for k in range(n) :
        for i in range(n):
            for j in range(n) :
                if graph[i][j] > graph[i][k] + graph[k][j] :
                    graph[i][j] = graph[i][k] + graph[k][j]
            
    return graph

graph = [[1e9] * n for _ in range(n)]

for i in range(n) :
    graph[i][i] = 0

while True :
    a,b = map(int,input().split())
    if a == -1 and b == -1 :
        break
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1
    
graph = floyd_warrshall(graph)

score = [max(i) for i in graph]
min_score = min(score)

candidate = [i+1 for i , j in enumerate(score) if j == min_score]

print(min_score, len(candidate))
print(' '.join(map(str,candidate)))


# 31120	32	


    
    