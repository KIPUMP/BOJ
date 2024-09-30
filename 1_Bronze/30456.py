# https://www.acmicpc.net/problem/30456
# 시간복잡도 생각 문제 → 답 조건만 성립하면 된다!
from collections import deque

n, p = map(int,input().split())
result = n

for i in range(1,p) :
    result += 10 ** i
    
print(result)

# 34008	64