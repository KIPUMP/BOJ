n = int(input())
switches = [0] + list(map(int, input().split())) # 인덱스 맞춰주기 위해
k = int(input())
arr = []

for _ in range(k):
    x, y = map(int, input().split())
    arr.append((x, y))

for x, y in arr:
    if x == 1: # 남학생이라면
        
        for i in range(y, n+1, y): # 받은 수의 배수인 스위치 번호에 대해서
                if switches[i] == 1 :
                    switches[i] = 0
                else :
                    switches[i] = 1
       
    else: # 여학생이라면
        check = []
        check.append(y)
        left = len(switches[1:y]) # 대칭의 왼쪽 부분
        right = len(switches[y+1:]) # 대칭의 오른쪽 부분
        min_len = min(left, right) # 둘 중에 짧은 부분의 길이 기준


        for i in range(1, min_len+1):
            if switches[y-i] == switches[y+i]: # 대칭이라면 append
                check.append(y-i)
                check.append(y+i)
            else:
                break # 대칭 아니면 break
        
        if len(check) >= 2: # 대칭이므로 무조건 2개 이상 들어가 있음
            for i in check:
                if switches[i] == 1 :
                    switches[i] = 0
                else :
                    switches[i] = 1
        
        else:               
            if switches[y] == 1 :
                switches[y] = 0
            else :
                switches[y] = 1
            
for i in range(1, n+1, 20):
    print(*switches[i:i+20])