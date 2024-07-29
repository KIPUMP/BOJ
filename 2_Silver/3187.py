# https://www.acmicpc.net/problem/9934
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

result = defaultdict(list)

def make_tree(arr,idx) :
    if len(arr) == 0 :
        return
    
    else :
        mid = len(arr)//2                       # 부모노드
        result[idx].append(arr[mid])
        
        left = arr[:mid]                        # 트리의 왼쪽
        make_tree(left,idx+1)
        
        right = arr[mid+1:]                     # 트리의 오른쪽
        make_tree(right,idx+1)
        
        

k = int(input())
arr = list(map(int,input().split()))

make_tree(arr,0)

for i in range(k) :
    print(*result[i])

#	34044	64