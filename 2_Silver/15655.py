# https://www.acmicpc.net/problem/15655
import sys
from itertools import combinations

n,m = map(int,input().split())
arr = sorted(map(int,input().split()))

for i in combinations(arr,m) :
    print(*i)
    

# 31120	32