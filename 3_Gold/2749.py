# https://www.acmicpc.net/problem/2749
# 피사노 주기 : 주기의 길이를 P라고 할 때,
# 피노나치 수를 M으로 나눈 나머지는 N & P번쨰 피보나치 수를 
# M으로 나눈 나머지와 같다. 
import sys

n = int(input())
dp = [0] * (1500050)

dp[1] = 1

for i in range(1500000) :
    dp[i+2] = (dp[i+1] + dp[i]) % 1000000


print(dp[n%1500000])


# 89940	408	