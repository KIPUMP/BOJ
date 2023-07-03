def GCD(x,y) :
  if y == 0 :
    return x

  else :
    return GCD(y,x%y)


T = int(input())

for _ in range(T) :
  a,b = map(int,input().split())
  result = (a*b) // GCD(a,b)
  print(result)
