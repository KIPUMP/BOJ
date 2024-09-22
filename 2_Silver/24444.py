# https://www.acmicpc.net/problem/24444
import sys
from collections import deque

input = sys.stdin.readline

c = 1
def bfs(start) :
    global c
    queue = deque()
    queue.append(start)
    visited[start] = c
    while queue :
        x = queue.popleft()
        for i in arr[x] :
            if visited[i] == 0 :
                c += 1
                visited[i] = c
                queue.append(i)
    


n,m,r = map(int,input().split())
arr = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m) :
    u,v = map(int,input().split())
    arr[u].append(v)
    arr[v].append(u)
    
for i in range(n+1) :
    arr[i].sort()
    
bfs(r)

for i in range(1,n+1) :
    print(visited[i])
    
# 58980	592