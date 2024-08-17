# https://www.acmicpc.net/problem/9471
# 피보나치 수열을 m으로 나누었을때의 주기를 구하는 문제

p = int(input())          # 테스트 케이스 개수
for i in range(p) :
  n,m = map(int,input().split())    # 테스트케이스 , m

  dp = [0] * 1000001
  dp[1] = 1
  dp[2] = 1
  for j in range(3,1000001) :       # 범위 내 피보나치 수 구하기
    dp[j] = (dp[j-1] + dp[j-2]) % m
    if dp[j-1] == 0 and dp[j] == 1 :
      print(i+1,j-1)
      break

# 56980	2208





