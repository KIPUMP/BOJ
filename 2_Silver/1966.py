from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())) :
    # n : 인쇄 페이지 수 , m : 몇번 째 놓여 있는지 인덱스
    n,m = map(int,input().split())             
    printer = list(map(int,input().split()))
    queue = deque()
    
    for i in range(n) :
        queue.append((i, printer[i]))       # 순번 인덱스 , printer 원소 삽입
    cnt = 1
    # print(queue)
    printer.sort()
    # print(printer)
    while queue :
        i, page = queue.popleft()
        token = True
        if page < printer[-1] :
            queue.append((i,page))
            token = False
        
        if token :
            
            printer.pop()
            
            if i == m :                 #  원하는 위치의 순번의 출력인지
                print(cnt)
                break
            
            cnt += 1                    
            
        
            
    
    