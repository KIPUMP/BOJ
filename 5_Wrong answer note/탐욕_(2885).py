# https://www.acmicpc.net/problem/2885

import sys
chocolates = [2 ** i for i in range(21)]

k = int(input())
choco = 0

for i in chocolates :
    if i >= k :
        choco = i
        break

result = choco
count = 0

while k > 0 :
    if k >= choco :
        k -= choco
        
    else :
        choco //= 2
        count += 1
        
print(result, count)

# 31120	32