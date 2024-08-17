# https://www.acmicpc.net/problem/16967

import sys

input = sys.stdin.readline

h,w,x,y = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(h+x)]

for i in range(x,h + x) :
    for j in range(y,w + y) : 
        arr[i][j] -= arr[i-x][j-y]          # x행, y열 만큼 움직인 만큼 원래 리스트에서 뺀다
        
for i in range(h) :
    for j in range(w) :
        print(arr[i][j], end=" ")
    print()
    
# 	37772	144