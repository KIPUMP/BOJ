# https://www.acmicpc.net/problem/1253
import sys
input = sys.stdin.readline


n = int(input())
arr = sorted(map(int,input().split()))      # 입력한 수를 정렬된 리스트에 넣는다
count = 0

for i in range(n) :
    target = arr[i]
    start , end = 0, n-1
    
    while start < end :
        
        if start == i :             # 자기 자신을 제외한 값으로 합을 구해야 함
            start += 1
            continue
        
        if end == i :               # 자기 자신을 제외한 값으로 합을 구해야 함
            end -= 1
            continue
        
        current_sum = arr[start] + arr[end]
        
        if current_sum == target :
            count += 1
            break
        
        elif current_sum < target :
            start += 1
            
        else :
            end -= 1
        
print(count)


# 31120	1084

