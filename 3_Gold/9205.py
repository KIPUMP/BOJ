# https://www.acmicpc.net/problem/9205
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x,arr) :
    visited[x] = True
    for i in range(len(arr)) :
        if not visited[i] and abs(arr[i][0] - arr[x][0]) + abs(arr[i][1] - arr[x][1]) <= 1000 :
            dfs(i,arr)

for _ in range(int(input())) :
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n+2)]
    visited = [False] * (n+2)
    
    dfs(0,arr)
    
    if not visited[-1] :
        print("sad")
        
    else :
        print("happy")


# 맞았습니다!!	31120	36