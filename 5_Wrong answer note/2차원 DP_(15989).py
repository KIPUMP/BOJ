# https://www.acmicpc.net/problem/15989
# 2차원 리스트를 사용해야 하는 DP 
import sys
input = sys.stdin.readline

dp = [[0] * 4 for _ in range(10001)]

dp[1][1] = 1                  # 초기값 (1)
dp[2][1] = 1                  # 1 + 1
dp[2][2] = 1                  # 2  
dp[3][1] = 1                  # 1 + 1 + 1
dp[3][2] = 1                  # 1 + 2
dp[3][3] = 1                  # 3

for j in range(4,10001) :
    
    dp[j][1] = dp[j-1][1]
    dp[j][2] = dp[j-2][1] + dp[j-2][2]
    dp[j][3] = dp[j-3][1] + dp[j-3][2] + dp[j-3][3]


t = int(input())
for i in range(1,t+1) :
    n = int(input())
    print(dp[n][1] + dp[n][2] + dp[n][3])

# 	32140	44