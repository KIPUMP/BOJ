# https://www.acmicpc.net/problem/1965
# if n >= 4 :d[n] = d[n-2] + d[n-3]    

for _ in range(int(input())) :          # 테스트 케이스
    n = int(input())                    # n 입력
    dp = [0] * (n+1)
    
    if n < 3 :                         # 3보다 작다면 (1 <= n 이므로 1)
        print(1)
    
    else : 
        dp[1] = 1                           # 초기값 셋팅
        dp[2] = 1
        
        for i in range(3,n+1) :             # 타뷸레이션
            dp[i] = dp[i-2] + dp[i-3]
        
        print(dp[n])
    
# 31120	52