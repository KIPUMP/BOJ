import sys

x = input()
cnt = 0

while len(x) >= 2 :
  num = 0
  for i in range(len(x)) :
    num += int(x[i])

  x = str(num)
  cnt += 1

print(cnt)
if int(x) % 3 == 0 :
  print("YES")

else :
  print("NO")
