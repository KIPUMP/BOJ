# https://www.acmicpc.net/problem/2018
# 해결  : 투 포인터(알고리즘 분류 참고)

n = int(input())
left, right = 0,0                 # 왼쪽 수 , 오른쪽 수

result = 0
total = 0

while left <= right or right <= n :         # 투 포인터 발생 조건
  
  if total == n :                           # 합이 n과 같다면,오른쪽 수 1 추가 후 합에 더한다
    result += 1                             
    right += 1
    total += right

  elif total > n :                          # 합이 n보다 크다면 왼쪽 수 빼고 왼쪽 수 1 증가
    total -= left
    left += 1
    
  else :                                    # 합이 n보다 작다면 오른쪽 수 1 키우고 오른쪽 수 더하기
    right += 1
    total += right

print(result)