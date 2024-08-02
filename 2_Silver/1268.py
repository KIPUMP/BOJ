# https://www.acmicpc.net/problem/1268

n = int(input())        # 학생수
students = [list(map(int,input().split())) for _ in range(n)]

student_count = [[0] * n for _ in range(n)]

# 열로 순회한다.
for i in range(5) :
  for j in range(n) :
    for k in range(n) :
      if students[j][i] == students[k][i] and j != k:
        student_count[j][k] = 1
        
sum_count = [0] * n

for idx, s in enumerate(student_count) :
      sum_count[idx] = s.count(1)
      
for i in range(n) :
      if sum_count[i] == max(sum_count) :
            print(i+1)
            break
          

# 38300	912