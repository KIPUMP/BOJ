arr = []
sum_val = 0
for _ in range(9) :
  arr.append(int(input()))

dept = sum(arr) - 100


for i in arr :
  for j in arr :
    if i+j == dept and i is not j :
      arr.remove(i)
      arr.remove(j)
      break
  if sum(arr) == 100 :
    break

arr.sort()

for i in arr :
  print(i)