import sys
input = sys.stdin.readline
timer = [300,60,10]

T = int(input())
result = []
for i in timer :
  result.append(T // i)
  T %= i

if T != 0 :
  print(-1)
else :
  for i in result :
    print(i,end=" ")