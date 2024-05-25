import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
result = []
arr.sort()

result.append(round((sum(arr)/n)))      # round(숫자) 소수점 0번째 자리에서 반올림
result.append(arr[(n//2)])

count = Counter(arr)
most_common = count.most_common()

max_freq = most_common[0][1]
modes = [num for num , freq in most_common if freq == max_freq]

if len(modes) > 1 :
  modes.sort()
  mode = modes[1]
else :
  mode = modes[0]
  
result.append(mode)
result.append(max(arr) - min(arr))

for i in result :
  print(i)


