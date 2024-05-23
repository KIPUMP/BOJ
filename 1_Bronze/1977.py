m = int(input())
n = int(input())

result = []
for i in range(m, n+1) :
  for j in range(1,101) :
    if j**2 == i :
      result.append(i)

if len(result) == 0 :
  print(-1)
else :
  print(sum(result))
  print(result[0])

    