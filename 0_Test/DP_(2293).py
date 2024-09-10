# https://www.acmicpc.net/problem/2293

n,k = map(int,input().split())
coins = [int(input()) for _ in range(n)]
dp = [0] * (k+1)

coins.sort()

for i in coins :
    dp[i] += 1
    
for i in range(k+1) :
    dp[i] +=



