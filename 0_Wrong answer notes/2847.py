# https://www.acmicpc.net/problem/2847

n = int(input())            # 레벨의 수
arr = [int(input()) for _ in range(n)]

next_level = arr[-1]       # 현재 레벨이 다음레벨보다 낮아야함                
idx = len(arr) - 2                  
count = 0
while True :
    if idx < 0 :           
        break 
    
    if next_level <= arr[idx] :             # 현재 레벨이 다음 레벨보다 1 작아지도록 조작
        arr[idx] -= 1
        count += 1
    else :
        next_level = arr[idx]
        idx -= 1

print(count)

# 31120	96


