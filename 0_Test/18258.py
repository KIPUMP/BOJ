# https://www.acmicpc.net/problem/18258
import sys
from collections import deque

input = sys.stdin.readline

queue = deque()
for _ in range(int(input())) :
    order = list(input().split())
    
    if len(order) == 2 :
        queue.append(order[1])
        
    else :
        if order[0] == "pop" :
            if len(queue) == 0 :
                print(-1)
            else :
                print(queue.popleft())
                
        elif order[0] == "size" :
            print(len(queue)) 
            
        elif order[0] == "empty" :
            if len(queue) == 0 :
                print(1)
            else :
                print(0)
                
        elif order[0] == "front" :
            if len(queue) == 0 :
                print(-1)
                
            else :
                print(queue[0])
                
        else :
            if len(queue) == 0 :
                print(-1)
                
            else :
                print(queue[-1])
        
# 143252	1804  → Java로도 한번 풀어볼것