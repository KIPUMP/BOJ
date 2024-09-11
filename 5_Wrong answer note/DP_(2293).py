# https://www.acmicpc.net/problem/2293
# https://velog.io/@jxlhe46/%EB%B0%B1%EC%A4%80-2293%EB%B2%88.-%EB%8F%99%EC%A0%84-1-bfi120m5

n,k = map(int,input().split())
coins = [int(input()) for _ in range(n)]
dp = [0] * (k+1)

coins.sort()

coins.reverse()

dp[0] = 1

for i in range(n) :
    for j in range(coins[i], k+1) :
        dp[j] += dp[j - coins[i]]

print(dp[k])


# 맞았습니다!!	31120	164