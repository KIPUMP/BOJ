n = int(input())
score = []
grade = []

for _ in range(n) :
  weight,height = map(int,input().split())
  score.append((weight,height))


for i in range(n) :
  cnt = 0
  for j in range(n) :
    if score[i][0] < score[j][0] and score[i][1] < score[j][1] :
      cnt += 1
  grade.append(cnt+1)

for i in grade :
  print(i,end=" ")



  