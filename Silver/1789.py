import sys
input = sys.stdin.readline
S = int(input())
sum_val = 0
arr = []
i = 1
while True :
  sum_val += i
  if sum_val > S:
    break
  arr.append(i)
  i+=1

print(max(arr))
