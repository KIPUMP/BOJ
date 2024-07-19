n = list(input().rstrip())
result = [0] * 10
for i in n :
  if int(i) == 6 or int(i) == 9 :
    if result[6] <= result[9] :
      result[6] += 1
    else :
      result[9] += 1

  else :
    result[int(i)] += 1

print(max(result))

