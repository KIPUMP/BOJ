# https://www.acmicpc.net/problem/13417
import sys
input = sys.stdin.readline

for _ in range(int(input())) :
    n = int(input())                        # 카드의 개수
    arr = list(input().split())            # 카드
    result = [arr[0]]
    arr = arr[1:]
    for i in range(len(arr)) :
        if ord(result[0]) < ord(arr[i]) :   # ASCII에서 맨 앞의 숫자보다 크다면 문장의 뒤로 
            result.append(arr[i])
        else :
            result = [arr[i]] + result      
    print(''.join(result))
    
# 31120	96