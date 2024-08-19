# https://www.acmicpc.net/problem/21939
from collections import defaultdict
import heapq, sys

input = sys.stdin.readline

max_h = []              # 최대 힙
min_h = []              # 최소 힙
solved = defaultdict(int)       # 푼문제 기록 딕셔너리

n = int(input())
for _ in range(n) :     # 최대 힙과 최소 힙에 원소 삽입
    p,l = map(int,input().split())
    heapq.heappush(max_h,(-l,-p))
    heapq.heappush(min_h,(l,p))
    
m = int(input())
for _ in range(m) :
    command = input().split()
    if command[0] == 'add' :
        heapq.heappush(max_h,(-int(command[2]),-int(command[1])))
        heapq.heappush(min_h,(int(command[2]),int(command[1])))
        
    elif command[0] == 'recommend' :
        if int(command[1]) == 1 :
            while solved[abs(max_h[0][1])] != 0:
                solved[abs(max_h[0][1])] -= 1
                heapq.heappop(max_h)
                
            print(-max_h[0][1])
            
        else :
            while solved[min_h[0][1]] != 0 :
                solved[min_h[0][1]] -= 1
                heapq.heappop(min_h)
                
            print(min_h[0][1])
            
    else :
        solved[int(command[1])] += 1
        

# 59664	216