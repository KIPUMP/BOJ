# https://www.acmicpc.net/problem/17144
import sys
input = sys.stdin.readline
# 미세먼지 확산
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def spread_dust() :
    global arr
    new_arr = [[0] * c for _ in range(r)]
    
    for i in range(r) :
        for j in range(c) :
            if arr[i][j] > 0 :
                dust = arr[i][j]
                spread_amount = dust // 5
                spread_count = 0
                
                for k in range(4) :
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < r and 0 <= ny < c :
                        if arr[nx][ny] == -1 :
                            new_arr[nx][ny] += spread_amount
                            spread_count += 1
                new_arr[i][j] += dust - (spread_amount * spread_amount)
                
    for row, col in purifiers :
        new_arr[row][col] = -1
        
    arr = new_arr
    
def top_clean() :
    x,y = purifiers[0]
    prev_value = 0
    
    for i in range(x-1,-1,-1) :
        arr[i+1][0], prev_value = prev_value, arr[i][0]
    
    for i in range(1,c) :
        arr[0][i-1], prev_value = prev_value, arr[0][i]
    
    for i in range(1,x+1) :
        arr[i-1][c-1], prev_value = prev_value, arr[i][c-1]
    
    for i in range(c-2,0,-1) :
        arr[x][i+1], prev_value = prev_value, arr[x][i]

def bottom_clean() :
    x,y = purifiers[1]
    prev_value = 0
    
    for i in range(x+1,r) :
        arr[i-1][0], prev_value = prev_value, arr[i][0]
        
    for i in range(1,c) :
        arr[r-1][i-1], prev_value = prev_value,arr[r-1][i]
        
    for i in range(r-2,x-1,-1) :
        arr[i+1][c-1], prev_value = prev_value, arr[i][c-1]
    for i in range(c-2,0,-1) :
        arr[x][i+1], prev_value = prev_value, arr[x][i]
        
r,c,t = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(r)]

purifiers = [(i,0) for i in range(r) if arr[i][0] == -1]

spread_dust()
top_clean()
bottom_clean()

total_dust = sum(sum(cell for cell in row if cell > 0) for row in arr)
print(total_dust)


