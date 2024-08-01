# https://www.acmicpc.net/problem/2108
import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
result = []
arr.sort()

result.append(round((sum(arr)/n)))                  # 산술 평균 
result.append(arr[(n//2)])                          # 중간값

count = Counter(arr)
most_common = count.most_common()                   # (원소,개수) 변환
max_freq = most_common[0][1]
modes = [num for num , freq in most_common if freq == max_freq]     #최대 개수의 원소만 담아준다

if len(modes) > 1 :
  modes.sort()
  mode = modes[1]
else :
  mode = modes[0]
  
result.append(mode)                                 
result.append(max(arr) - min(arr))

for i in result :
  print(i)


# 52748	536