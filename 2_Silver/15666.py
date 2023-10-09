from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
result = []
for i in combinations_with_replacement(arr,m) :
  if i not in result :
    result.append(i)
for i in result :
  print(*i)
