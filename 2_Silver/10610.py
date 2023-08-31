# 해당수가 N의 배수인지 알려면 , 모든 자릿수의 합이 N의 배수이면 된다.
import sys
input = sys.stdin.readline
N = input()
N = sorted(N,reverse = True)
sum_val = 0
if '0' not in N :

  print(-1)
else :
  for i in N :
    sum_val += int(i)
  if sum_val % 3 != 0 :
    print(-1)
  else :
    print("".join(N))