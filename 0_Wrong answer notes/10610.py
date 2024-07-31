# https://www.acmicpc.net/problem/10610
# 정렬후 모든 수의 합이 3의 배수가 되어야 함
n = input()

# 가장 큰 30의 배수를 만들기 위해 숫자를 리스트로 내림차순 정렬
n = sorted(n,reverse = True)
# 0이 없으면 30의 배수가 될 수 없음
sum_val = 0

if '0' not in n :
  print(-1)

else :
  for i in n :
    sum_val += int(i)
    
  if sum_val % 3 != 0 :
    print(-1)
    
  else :
    print("".join(n))