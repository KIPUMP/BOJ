import heapq

min_heap = []                   # 최소 힙
heapq.heappush(min_heap,5)
heapq.heappush(min_heap,1)
heapq.heappush(min_heap,3)
print(heapq.heappop(min_heap))              

max_heap = []                   # 최대 힙
heapq.heappush(max_heap,-5)
heapq.heappush(max_heap,-1)
heapq.heappush(max_heap,-3)
print(-heapq.heappop(max_heap))