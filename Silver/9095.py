import sys
input = sys.stdin.readline
T = int(input())
def plus_num(n) :
  if n == 1 :
    return 1  
  elif n == 2 :
    return 2 
  elif n == 3 :
    return 4

  else :
    return plus_num(n-1) + plus_num(n-2) + plus_num(n-3)

for _ in range(T) :
  n = int(input())
  print(plus_num(n))
