n = int(input())
for i in range(n) :
  total = 0
  while i > 0  :
    total += i % 10
    i //= 10
  
  if n == i + total :
    print(i)
    break
