import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = [list(map(int,input().strip())) for _ in range(n)]
dx = [0,1,1]
dy = [1,1,0]
max_square = 1
for i in range(n) :
    for j in range(m) :
        for k in range(1,n) :
            temp = arr[i][j]
            cnt = 0
            for l in range(3) :
                nx = i + dx[l] * k 
                ny = j + dy[l] * k
                if 0 <= nx < n and 0 <= ny < m :
                    if temp == arr[nx][ny] :
                        cnt += 1
                        
            if cnt == 3 :
                max_square = max(max_square,(k+1)**2)
                
print(max_square)
                
            
        
        
        
        
        