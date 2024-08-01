# https://www.acmicpc.net/problem/18111

import sys
input = sys.stdin.readline

# 평균 구하기
def get_avg(arr) :
    sum_val = 0
    
    for i in range(n) :
        sum_val += sum(arr[i])
    
    avg  = sum_val // (n*m)

    avg_down = 0 

    for i in range(n) :
        for j in range(m) :
            if avg > arr[i][j] :
                avg_down += 1
    
    if avg_down <= b :
        avg += 1
        
    return avg

def solution(arr,avg) :
    global b, result
    token = False
    while True :
        if token :
            break
        
        for i in range(n) :
            for j in range(m) :
                if arr[i][j] == avg :
                    token = True
                else :
                    token = False
                    if arr[i][j] < avg :
                        arr[i][j] += 1
                        b -= 1
                        result += 1
                    else :
                        arr[i][j] -= 1
                        b += 1
                        result += 2
                            
    return arr
                            
n,m,b = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
sum_val = 0

result = 0
avg = get_avg(arr)
arr = solution(arr,avg)
print(result,arr[0][0])