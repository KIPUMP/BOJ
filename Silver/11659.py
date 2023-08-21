import sys
input = sys.stdin.readline
N,M = map(int,input().split())
num = list(map(int,input().split()))
num_sum = [0]
temp = 0
for i in num:
  temp += i
  num_sum.append(temp)

for _ in range(M) :
  i,j = map(int,input().split())
  print(num_sum[j] - num_sum[i-1])