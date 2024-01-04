from collections import deque
for _ in range(int(input())) :
    n,m = map(int,input().split())
    printer = deque(map(int,input().split()))
    cnt = 0
    
    while printer :
        priority_page = max(printer)
        front_page = printer.popleft()
        m -= 1
        
        if front_page == priority_page :
            cnt += 1
            if m < 0 :
                print(cnt)
                break
        else :
            printer.append(front_page)
            if m < 0 :
                m = len(printer) - 1
            
    