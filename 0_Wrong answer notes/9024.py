import sys
input = sys.stdin.readline


def solution(arr, n, k) :      # 정렬된 배열과 기준 정수 k
  start, end = 0 , n - 1   #  시작, 끝 인덱스
  sum_val = arr[start] + arr[end]
  result = 1e9
  cnt = 0
  
  while start < end :
    sum_val = arr[start] + arr[end]
    omit = abs(k - sum_val)     # 오차 

    if result > omit :
      result = omit
      cnt = 1

    elif result == omit :
      cnt += 1
    
    if sum_val < k :                # 합계가 k 보다 작다면 값을 키워야 한다.
      start += 1
    else :                          # 같거나 크다면 값을 줄여야 한다
      end -=1

  return cnt

for _ in range(int(input())):
  n,k = map(int,input().split())    # 리스트 크기, 기준 정수  k
  arr = sorted(map(int,input().split()))

  print(solution(arr,n,k))