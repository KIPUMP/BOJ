import sys
from itertools import combinations
sys.setrecursionlimit(10**6)
def GCD(x,y) :
  if y == 0 :
    return x 
  else :
    return GCD(y,x%y)

for _ in range(int(input())) :
  nums = list(map(int,input().split()))
  result = []
  for i in combinations(nums,2) :
    x,y = i
    result.append(GCD(x,y))
  
  print(max(result))
