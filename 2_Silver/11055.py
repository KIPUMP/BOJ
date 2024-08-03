# https://www.acmicpc.net/problem/11055

n = int(input())
arr = list(map(int,input().split()))

dp = [0] * (n+1)               # 증가하는 리스트의 합을 기억하는 리스트

for i in range(n) :
    dp[i] = arr[i]             # dp 값 초기화          

for i in range(n) :                 
    for j in range(i) :
        if arr[i] > arr[j] :
            dp[i] = max(dp[i], dp[j]+arr[i])         # dp값 비교

print(max(dp))


#31120	168