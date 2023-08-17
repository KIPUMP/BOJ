import sys
input = sys.stdin.readline
N = int(input())
bag = 0
while N > 2 :

  if N % 3 == 0 and N % 5 != 0: 
    N -= 3
    bag += 1

  else :
    N -= 5
    bag += 1

if N == 0 :
  print(bag)
else :
  print(-1)