arr = []
for i in range(9) :
  n = int(input())
  arr.append(n)

max = arr[0]
for i in arr :
  if i > max :
    max = i


print(max)
print(arr.index(max)+1)
