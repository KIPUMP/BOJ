# https://www.acmicpc.net/problem/9375
import sys
from collections import defaultdict

input = sys.stdin.readline

for _ in range(int(input())) :      # 테스트 케이스
  n = int(input())                  # 의상 수 
  arr = defaultdict(int)
  for i in range(n) :
    garment, category = input().split()
    arr[category] += 1

  cnt = 1
  for i in arr.values() :
    cnt *= i + 1                    # 규칙 (n종류의 가짓수 m 있을 때 (m+1)*....(n번 반복) -1)

  print(cnt-1)

#34000	60