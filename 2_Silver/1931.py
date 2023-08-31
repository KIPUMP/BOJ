import sys
input = sys.stdin.readline
N = int(input())
lesson = []
cnt = 0 
for _ in range(N) :
  lesson.append(tuple(map(int,input().split())))
lesson = sorted(lesson,key = lambda x : (x[1],x[0]))
t = 0
for start,end in lesson:
  if t <= start :
    cnt += 1
    t = end 
print(cnt)
  

