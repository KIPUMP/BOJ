# https://www.acmicpc.net/problem/1268

n = int(input())        # 학생수
students = [list(map(int,input().split())) for _ in range(n)]

student_count = [[0] * n for _ in range(5)]

# 열로 순회한다.
for i in range(5) :
  for j in range(n) :
    for k in range(n) :
      if students[j][i] == students[k][i] and j != k :
        student_count[][] +=1

# 완성돤 dict()를 내림차순으로 정렬
student_list = sorted(student_count.items(), key = lambda x : (-x[1],x[0]))

print(student_list[0][0])
