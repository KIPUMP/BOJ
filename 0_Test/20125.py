# https://www.acmicpc.net/problem/20125
import sys
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [-1,1,0,0]

def find_heart(x,y) :
    token = False
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n :
            if arr[nx][ny] == '*' :
                token = True
            else :
                token = False
                break
    
    if token :
        return (x,y)
    else :
        return (-1,-1)


n = int(input())

arr = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]


result = []
for i in range(n) :
    for j in range(n) :
        x,y = find_heart(i,j)
        
        if x > -1 and y > -1:
            print(x+1,y+1)
            visited[x][y] = True
            for l in range(4) :
                count = 0
                for m in range(1,n) :
                    nx = x + dx[l] * m
                    ny = y + dy[l] * m 
                    
                    if 0 <= nx < n and 0 <= ny < n :
                        if not visited[nx][ny] and arr[nx][ny] == '*'  :
                            count += 1
                            visited[nx][ny] = True
                            
                    else : 
                        result.append(count)
                        break
                            
        if len(result) == 4 :
            break
    
    if len(result) == 4 :
        break
                            

result.pop()

for i in range(n) :
    for j in range(n) :
        if not visited[i][j] and arr[i][j] == '*'  :
            count = 1
            for k in range(1,n) :
                nx = i + dx[2] * k
                ny = j + dy[2] * k
                
                if 0 <= nx < n and 0 <= ny < n :
                    if arr[nx][ny] == '*' :
                        visited[nx][ny] = True
                        count += 1
                        
                else :
                    result.append(count)
                    break
                        
        
print(*result)


# 맞았습니다!!	46312	644