# 코딩테스트 2주차
# https://www.acmicpc.net/problem/13975

import sys,heapq
input = sys.stdin.readline

for _ in range(int(input())) :
    n = int(input())                        # 책 권수
    arr = list(map(int,input().split()))    # 책 정보 리스트
    total = 0                               # 출력
    book = []                               # 책 heap
    for i in range(n) :
        heapq.heappush(book,arr[i])

    while len(book) > 1 :
        x = heapq.heappop(book)
        y = heapq.heappop(book)
        
        total += x+y
        
        heapq.heappush(book,(x+y))
        
    print(total)
    
    
    
# 185112	5284