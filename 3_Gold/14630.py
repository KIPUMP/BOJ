# https://www.acmicpc.net/problem/14630
import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def calculate_cost(str1, str2):
    cost = 0
    for c1, c2 in zip(str1, str2):
        cost += (int(c1) - int(c2)) ** 2
    return cost

def dijkstra(start, end):
    distance = [INF] * (n+1)
    distance[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    
    while pq:
        weight, node = heapq.heappop(pq)
        
        if weight > distance[node]:
            continue
        
        for neighbor in range(1, n+1):
            if neighbor != node:
                # 필요한 경우에만 비용 계산
                cost = calculate_cost(costs[node], costs[neighbor])
                if distance[neighbor] > weight + cost:
                    distance[neighbor] = weight + cost
                    heapq.heappush(pq, (distance[neighbor], neighbor))
                
    return distance[end]

n = int(input())
costs = ['']  # index를 1부터 맞추기 위해서
for i in range(n):
    costs.append(input().strip())

before, after = map(int, input().split())

result = dijkstra(before, after)

print(result)


# 112500	1744(pypy)