from collections import deque
n = int(input())
start, end = map(int,input().split())
m = int(input())
arr = [[] for _ in range(n+1)]

for i in range(m) :
    x,y = map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)

cnt = [0] * (n+1)
queue = deque()

def bfs(node) :
    queue.append(node)
    while queue :
        node = queue.popleft()
        for i in arr[node] :
            if cnt[i] == 0 :
                cnt[i] = cnt[node] + 1
                queue.append(i)
bfs(start)

if cnt[end] > 0 :
    print(cnt[end])
else :
    print(-1)
    