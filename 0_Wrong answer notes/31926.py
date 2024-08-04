# https://www.acmicpc.net/problem/31926
import math
count = 8  # 초기 고정값

n = int(input())  # 사용자로부터 입력 받기

idx =  1

while True :
    if n - math.pow(2,idx) < 0 :
        count = count + idx + 1
        break
    
    elif n - math.pow(2,idx) == 0 :
        count = count + idx + 2
        break
    
    idx += 1
    
print(count)

# 	33240	32