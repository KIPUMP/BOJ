# https://www.acmicpc.net/problem/11404

def floyd_warshall(arr) :
    for k in range(n) :
        for i in range(n) :
            for j in range(n) :
                if arr[i][k] < int(1e9) and arr[k][j] < int(1e9) :
                    arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
    return arr

n = int(input())
m = int(input())
arr = [[int(1e9)] * n for _ in range(n)]

for _ in range(m) :
    a,b,c = map(int,input().split())
    if arr[a-1][b-1] > c :
        arr[a-1][b-1] = c
    
for i in range(n) :
    arr[i][i] = 0    
    
arr = floyd_warshall(arr)

for i in range(n) :
    for j in range(n) :
        if arr[i][j] == int(1e9) :
            arr[i][j] = 0
            
for i in range(n) :
    print(*arr[i])

# 31120	2876