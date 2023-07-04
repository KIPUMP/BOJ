arr = []

for i in range(1,10001) :
  for j in str(i) :
    i += int(j) 
  arr.append(i)

for i in range(1,10001) :
  if i not in arr :
    print(i)
