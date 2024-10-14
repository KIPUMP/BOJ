# https://www.acmicpc.net/problem/1389
import sys
input = sys.stdin.readline

def floyd_warshall(arr) :
    for k in range(n) :
        for i in range(n) :
            for j in range(n) :
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
    
    return arr                
                


n,m = map(int,input().split())  # 친구 수, 친구 관계 수

friendship = [[int(1e9)] * n for _ in range(n)]

for _ in range(m) :
    a,b = map(int,input().split())
    friendship[a-1][b-1] = 1
    friendship[b-1][a-1] = 1
    
x = floyd_warshall(friendship)

result = []
for i in range(n) :
    result.append(sum(x[i]))

print(result.index(min(result))+1)


# 31120	228
