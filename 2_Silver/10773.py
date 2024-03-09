import sys
input = sys.stdin.readline
arr = []
for _ in range(int(input())) :
  x = int(input())
  if x == 0 :
    arr.pop()
  else :
    arr.append(x)

result = 0
for i in range(len(arr)) :
  result += arr[i]

print(result)
  

  