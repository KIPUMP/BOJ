# https://www.acmicpc.net/problem/25622
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(node):
    global groups
    visited[node] = True
    groups.append(node+1)
    if len(groups) == 3 : 
        result.append(groups)
        groups = []
    for neighbor in tree[node]:
        if not visited[neighbor]:
            dfs(neighbor)
                
# 입력 처리
n = int(input())  # 역의 개수
tree = [[] for _ in range(n)]
visited = [False] * n

groups = []
result = []

# 트리 구성
for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u-1].append(v-1)
    tree[v-1].append(u-1)
    
dfs(tree[0][0])

print(result)