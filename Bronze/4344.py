c = int(input())

for _ in range(c) :
  arr = list(map(int,input().split()))
  n = arr[0]
  student = arr[1:]
  avg = sum(student) / n
  cnt = 0
  for i in range(1,n+1) :
    if arr[i] > avg :
      cnt += 1
  student_percent = (cnt/n) * 100

  print(f"{student_percent:.3f}%")
  
  


