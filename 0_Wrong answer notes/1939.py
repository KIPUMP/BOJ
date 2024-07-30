# https://www.acmicpc.net/problem/1939

import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, end, weight_limit):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    
    while queue:
        current = queue.popleft()
        
        if current == end:
            return True
        
        for next_node, next_weight in graph[current]:
            if not visited[next_node] and next_weight >= weight_limit:
                visited[next_node] = True
                queue.append(next_node)
    
    return False

def binary_search():
    low, high = 1, 1000000000               # 중량 제한 범위 설정
    result = low                            # 
    
    while low <= high:
        mid = (low + high) // 2
        if bfs(start, end, mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return result

n, m = map(int, input().split())  # 점, 간선

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())  # 섬 A, 섬 B, 간선 C
    graph[a].append((b, c))
    graph[b].append((a, c))

start, end = map(int, input().split())  # 공장 위치 좌표

print(binary_search())

# 57180	496