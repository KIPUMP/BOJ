# https://www.acmicpc.net/problem/24479

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m,r = map(int,input().split())
arr = [[] for _ in range(n+1)]
visited = [0] * (n+1)

c = 1

def dfs(start) :
    global c
    visited[start] = c
    for i in arr[start] :
        if visited[i] == 0 :
            c+=1
            dfs(i)

for _ in range(m) :
    u,v = map(int,input().split())
    arr[u].append(v)
    arr[v].append(u)
    
for i in range(n+1) :
    arr[i].sort()
        
dfs(r)

for i in range(1,n+1) :
    print(visited[i])

# 67996	560
