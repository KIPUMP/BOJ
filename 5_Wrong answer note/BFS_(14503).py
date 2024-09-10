# https://www.acmicpc.net/problem/14503
import sys
input = sys.stdin.readline

# d가 0일 때 북, 동, 남 , 서 
dx = [-1, 0, 1, 0]          
dy = [0, 1, 0, -1]

def turn_left(d) :
    return (d - 1) % 4          # 반시계 방향 

def bfs(x,y,d) :
    visited[x][y] = True
    result = 1
    
    while True :
        found_new_place = False
        for _ in range(4) :
            d = turn_left(d)
            nx = x + dx[d]
            ny = y + dy[d]
            
            if 0 <= nx < n and 0 <= ny < m :
                if not visited[nx][ny] and arr[nx][ny] == 0 :
                    visited[nx][ny] = True
                    x,y = nx, ny
                    result += 1
                    found_new_place = True
                    break
                
        if not found_new_place :
            back_direction = (d + 2) % 4        # 바라보는 방향으로 뒤로
            nx = x + dx[back_direction]
            ny = y + dy[back_direction]
            
            if arr[nx][ny] == 0 :
                x,y = nx,ny
                
            else :
                break
    return result

n,m = map(int,input().split())
r,c,d = map(int,input().split())            # 시작 좌표, 방향
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

print(bfs(r,c,d))
            

# 맞았습니다!!	31120	40