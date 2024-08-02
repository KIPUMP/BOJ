# https://www.acmicpc.net/problem/2631
# LIS를 통해 최대 길이의 증가 리스트를 찾은후 리스트 길이의 차를 구한다

n = int(input())
arr = []
for _ in range(n) :
    arr.append(int(input()))

dp = [1] * (n+1)            # dp 초기화

for i in range(n) :
    for j in range(i) :
        if arr[j] < arr[i] :
            dp[i] = max(dp[i],dp[j] + 1)
            
print(n - max(dp))               


# 31120	56	