# https://www.acmicpc.net/problem/2839
# 풀이 : 탑욕법 
n = int(input())
bags = [3,5]
cnt = 0
while n > 2 :
  if n % bags[0] == 0 and n % bags[1] != 0 :        # 가방의 개수를 최소로 줄이는 것이 목표이므로 3으로 먼저 나눈다.
    n -= bags[0]
    cnt += 1
  else :
    n -= bags[1]
    cnt += 1

if n == 0 :
  print(cnt)
else :
  print(-1)