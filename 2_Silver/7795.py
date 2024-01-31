import sys
input = sys.stdin.readline

for _ in range(int(input())) :
    
    n,m = map(int,input().split())
    
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    
    a.sort()        # 1 1 3 7 8 
    b.sort()        # 1 3 6
    
    start = 0
    result = 0
    
    for i in range(n) :
        start = 0
        while True :
            if start == m or a[i] <= b[start] :
                result += start
                break
            else :
                start += 1
    
    print(result)
                
                