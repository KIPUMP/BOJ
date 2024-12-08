# https://www.acmicpc.net/problem/10845
import sys

input = sys.stdin.readline
arr = []
for _ in range(int(input())) :
    order = list(input().split())
    if len(order) == 1 :
        if order[0] == "pop" :
            if len(arr) == 0 :
                print(-1)
            else :
                print(arr[0])
                arr = arr[1:]
            
        elif order[0] == "size" :
            print(len(arr))
            
        elif order[0] == "empty" :
            if len(arr) == 0 :
                print(1)
            else :
                print(0)
                
        elif order[0] == "front" :
            if len(arr) == 0 :
                print(-1)
            else :
                print(arr[0])
                
        else :
            if len(arr) == 0 :
                print(-1)
            else :
                print(arr[-1])
                
                
    else :
        arr.append(order[1])
            
# 33432	40