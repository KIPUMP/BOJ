# https://www.acmicpc.net/problem/5014
import sys
from collections import deque

def bfs(x) :
    queue = deque()
    visited[x] = True
    queue.append(x)
    while queue :
        x = queue.popleft()
        for i in range(2) :
            nx = x + move[i] * ((-1) ** (2 + i))
            
            if 0 < nx <= f :
                if not visited[nx] :
                    visited[nx] = True
                    arr[nx] = arr[x] + 1
                    queue.append(nx)

f,s,g,u,d = map(int,input().split())
arr = [0] *(f+1)
move = [u,d]
visited = [False] * (f+1)

bfs(s)

if arr[g] == 0 and not visited[g] :
    print("use the stairs")
else :
    print(arr[g])
    
    
# 79620	784

