from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
arr_1 = list(map(int,input().split()))
m = int(input())
arr_2 = list(map(int,input().split()))

card = defaultdict(int)

for i in range(n) :
    card[arr_1[i]] += 1
    
result = []

for i in range(m) :
    if card[arr_2[i]] == 0  :
        result.append(0)
    else :
        result.append(card[arr_2[i]])
        
print(*result)