import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort()
B.reverse()
sum_val = 0
for i in range(N) :
  add_num = A[i] * B[i]
  sum_val += add_num

print(sum_val)
  
