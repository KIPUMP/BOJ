# https://www.acmicpc.net/problem/1268

n = int(input())        # 학생수
students = [list(map(int,input().split())) for _ in range(n)]

student_count = [[0] * n for _ in range(5)]

# 열로 순회한다.
for i in range(5) :
  for j in range(n) :
    for k in range(j+1,n) :
      if students[j][i] == students[k][i] :
        student_count[k][j] = 1
        student_count[j][k] = 1

cnt = []

for i in student_count :
  cnt.append(i.count(1))

print(cnt.index(max(cnt))+1)