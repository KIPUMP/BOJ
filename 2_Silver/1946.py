# https://www.acmicpc.net/problem/1946
# 1차 서류 심사 최소 점수인 지원자들부터 2차 면접 점수를 비교
import sys
input = sys.stdin.readline

for _ in range(int(input())):
  n = int(input())
  cnt = 1             # 최대 선발 지원자(무조건 1명은 있다)
  score = [list(map(int,input().split())) for _ in range(n)]             # 1,2차 점수
  score= sorted(score, key = lambda x : x[0])
  top = 0
  for i in range(1, n) :
    if score[i][1] < score[top][1] :
      top = i
      cnt += 1

  print(cnt)

  
      
#72128	4184
