# https://www.acmicpc.net/problem/11047

import sys
input = sys.stdin.readline

n,k = map(int,input().split())
coins = []
for _ in range(n) :
    coins.append(int(input()))
    
coins = sorted(coins,reverse=True)
count = 0
for i in coins :
    count += k // i
    k %= i
    
print(count)

# 31120	36