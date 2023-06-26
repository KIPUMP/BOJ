def plus_num(x) :
  if x % 10 == x :
    return x
  else :
    return plus_num(x//10) + (x % 10)

n = int(input())
arr= []
for i in range(n) :
  if n == i + plus_num(i) :
    arr.append(i)

if len(arr) == 0 :
  print(0)
else :
  print(min(arr))