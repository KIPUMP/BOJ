# https://www.acmicpc.net/problem/15723
import sys
input = sys.stdin.readline

def floyd_warshall(graph) :
    for k in range(26) :
        for i in range(26) :
            for j in range(26) :
                if graph[i][k] and graph[k][j] :
                    graph[i][j] = True
    return graph
                    


n = int(input())
graph = [[False]* (26) for _ in range(26)]
for _ in range(n) :
    logic = list(input().split())
    graph[ord(logic[0]) - ord('a')][ord(logic[2]) - ord('a')] = True

graph = floyd_warshall(graph)

result = []
m = int(input())
for _ in range(m) :
    theory = list(input().split())
    if graph[ord(theory[0])- ord('a')][ord(theory[2]) - ord('a')] :
        result.append("T")
    else :
        result.append("F")
        
print("\n".join(result))
    