# 코딩테스트 2주차
# https://www.acmicpc.net/problem/1697
from collections import deque

def bfs(n, k):
    queue.append(n)
    while queue:
        current = queue.popleft()

        if current == k:
            return d[current]

        distance = []
        
        distance.append(current * 2)            # 수빈 순간 이동
        distance.append(current - 1)            # 수빈 이동
        distance.append(current + 1)            # 수빈 이동
        
        for i in distance:
            if 0 <= i < max_range and d[i] == -1:
                d[i] = d[current] + 1
                queue.append(i)

max_range = 100001

# 수빈 위치 , 동생 위치
n, k = map(int, input().split())             

# 방문 여부 및 걸린 시간을 저장하는 리스트
d = [-1] * (max_range)

d[n] = 0

queue = deque()
print(bfs(n, k))

# 34972	108