# https://www.acmicpc.net/problem/10610
# 정렬후 모든 수의 합이 3의 배수가 되어야 함
n = input()

n = sorted(n,reverse = True)
# 0이 없으면 30의 배수가 될 수 없음
sum_val = 0

if '0' not in n :
  print(-1)

else :
  for i in n :
    sum_val+= int(i)
  if sum_val % 3 != 0 :
    print(-1)
  else :
    print("".join(n))