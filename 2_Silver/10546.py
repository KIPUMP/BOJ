# https://www.acmicpc.net/problem/10546

import sys
from collections import defaultdict
input = sys.stdin.readline

marathon = defaultdict(int)

n = int(input())

for _ in range(2*n-1) :
    name = input()
    marathon[name] += 1
    

for i in marathon.keys() :
    if marathon[i] % 2 != 0 :
        print(i)
        break
    
# 45040	192