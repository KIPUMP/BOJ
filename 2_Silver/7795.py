import sys
input = sys.stdin.readline

for _ in range(int(input())) :
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    start = 0
    result = 0
    
    for i in range(n) :
        while True :
            if start == m or a[i] <= b[start] :
                result += start
                break
            else :
                start += 1
    
    print(result)
                
                