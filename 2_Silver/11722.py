# https://www.acmicpc.net/problem/11722

n = int(input())
arr = list(map(int,input().split()))

dp = [1] * (n+1)                    # 값 초기화

for i in range(n) :     
    for j in range(i) :
        if arr[j] > arr[i] :        # i 보다 앞에 있는 값이 크다면 dp 값 비교하여 최신화
            dp[i] = max(dp[i],dp[j] + 1)
            
    
print(max(dp))

# 31120	168