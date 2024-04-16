import sys
input = sys.stdin.readline

for _ in range(int(input())) :
  j,n = map(int,input().split())
  area = []
  result = 0
  for _ in range(n) :
    r,c = map(int,input().split())
    area.append(r*c)

  area.sort()
  area.reverse()
  for i in range(n) :
    j -= area[i]
    result += 1
    if j <= 0 :
      break

  print(result)