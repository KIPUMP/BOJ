# https://www.acmicpc.net/problem/13549
import sys
from collections import deque

dx = [1,-1,2]

def bfs(start) :
    queue = deque()
    arr[start] = 0
    queue.append(start)
    
    while queue :
        x = queue.popleft()
        for i in range(3) : 
            if dx[i] == 2 :
                nx = x * dx[i]
                if 0 <= nx < 100001 :
                    if arr[x] < arr[nx] :
                        arr[nx] = arr[x]
                        queue.append(nx)
            else :
                nx = x + dx[i]
                if 0 <= nx < 100001 :
                    if arr[x] + 1 < arr[nx] :
                        arr[nx] = arr[x] + 1
                        queue.append(nx)
                
                
            

n,k = map(int,input().split())
# total_len = (max(n,k) + 1) 
arr = [int(1e9)] * 100001       # 수빈이와 동생이 있는 공간(list) 정의

bfs(n)

print(arr[k])

# 37340	128