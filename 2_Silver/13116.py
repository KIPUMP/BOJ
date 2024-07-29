# https://www.acmicpc.net/problem/13116
# a,b 중 큰 수 // 2 해서 값을 계속 비교하여 같아지는 순간을 확인한다.
import sys
input = sys.stdin.readline

for _ in range(int(input())) :
    a,b = map(int,input().split())

    while True :
        if a == b :
            print(a * 10)
            break
        if a < b :              # b가 큰 경우 
            b //= 2
        else :                  # a가 큰 경우
            a //= 2
            
    
# 31120	208
    
    