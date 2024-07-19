# https://www.acmicpc.net/problem/2705

dp = [1,2,2,4,4]

for _ in range(int(input())) :
    n = int(input())
    
    if n <= len(dp) :
        print(dp[n-1])
        
    else :
        for i in range(len(dp),n) :
            if i // 2  :
                dp.append(dp[(i-1)//2] + dp[i-2])
            else :
                dp.append(dp[i-1] + 2)
        print(dp[n-1])
            
