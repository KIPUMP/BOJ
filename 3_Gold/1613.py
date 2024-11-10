# https://www.acmicpc.net/problem/1613
import sys

input = sys.stdin.readline

    
n,k = map(int,input().split())

arr = [[int(1e9)] * n for  _ in range(n)]

for i in range(k) :
    a,b = map(int,input().split())
    arr[a-1][b-1] = 1
    
for k in range(n) :
    for i in range(n) :
        for j in range(n) :
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])


for _ in range(int(input())) :
    a,b = map(int,input().split())

    if arr[a-1][b-1] == arr[b-1][a-1] :
        print(0)
        
    elif arr[a-1][b-1] < arr[b-1][a-1] :
        print(-1)
        
    else :
        print(1)
        
# 112768	712 (pypy)