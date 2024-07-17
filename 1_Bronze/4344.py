# https://www.acmicpc.net/problem/4344
# 평균이 넘는 학생들의 비율을 소수점 셋째 자리까지 출력

c = int(input())                    # 테스트 켸이스 수 입력

for _ in range(c) :
  arr = list(map(int,input().split()))      # 배열 입력
  
  n = arr[0]                                # 학생 수
  students = arr[1:]                        # 학생 점수 정보
  
  avg = sum(students) / n                   # 평균
  cnt = 0
  for i in range(n) :                       # 학생이 평균이 넘는지 확인한다
      if students[i] > avg :                
        cnt += 1
  
  print(f"{((cnt/n)*100):.3f}%")            # 평균 넘는 학생 비율 소수점 3자리 까지 출력
  