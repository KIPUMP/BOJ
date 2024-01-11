import heapq
n,m = map(int,input().split())
card = list(map(int,input().split()))
heapq.heapify(card)

for i in range(m) :
    x = heapq.heappop(card)
    y = heapq.heappop(card)
    sum_val = x+y
    heapq.heappush(card,sum_val)
    heapq.heappush(card,sum_val)
    
print(sum(card))