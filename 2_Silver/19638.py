# https://www.acmicpc.net/problem/19638
import sys
import heapq
input = sys.stdin.readline

# 거인 인구수, 센티 키, 뿅망치 사용수
n,h,t = map(int,input().split())           
giant = []
cnt = 0                     # 뿅망치 횟수
for _ in range(n) :
    heapq.heappush(giant,(int(input())*(-1)))       # max heap 구현

if giant[0] * (-1) < h :                           # 첫번째 비교
    print("YES")
    print(cnt)
    sys.exit()
    
for _ in range(t) :    
    giant_height = -heapq.heappop(giant)
    
    if giant_height == 1 :                  # 모든 원소가 1
        print("NO")
        print(giant_height)
        sys.exit()
        
    heapq.heappush(giant, (-1) * (giant_height // 2))  
    cnt += 1
    
    if giant[0] * (-1) < h :                       # 줄이고 난 후 비교
        print("YES")
        print(cnt)
        sys.exit()
    

if giant[0] * (-1) >= h :
    print("NO")
    print(-heapq.heappop(giant))
    
# 39092	184