import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

compare_node = arr[-1]          # 비교 노드 선언

count = 1
for i in range(n-2,-1,-1) :
    if arr[i] > compare_node :
        count += 1
        compare_node = arr[i]       # 비교 노드 최신화
        
        
print(count)