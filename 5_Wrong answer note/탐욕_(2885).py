# https://www.acmicpc.net/problem/2885

import sys
chocolates = [2 ** i for i in range(21)]   # 초콜릿 크기 리스트

k = int(input())
choco = 0

for i in chocolates :                      # 초콜릿 최소 크기 찾기
    if i >= k :
        choco = i
        break

result = choco
count = 0

while k > 0 :
    if k >= choco :                         # 크기가 작다면 뺀다
        k -= choco
        
    else :
        choco //= 2                         # 반으로 나눈 후 count++
        count += 1
        
print(result, count)

# 31120	32