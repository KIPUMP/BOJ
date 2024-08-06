import sys
input = sys.stdin.readline

# 방향리스트(상,하,좌,우,대각선)
dx = [-1,-1,1,0]
dy = [-1,1,0,1]


# 빙고 판 입력
arr = [list(map(int,input().split())) for _ in range(5)]     

# 방문 처리 리스트 
visited = [[False] * 5 for _ in range(5)]
# 빙고 처리 함수 (사회자가 부른 숫자)  
def bingo(n) :
    for i in range(5) :
        for j in range(5) :
            if arr[i][j] == n :
                visited[i][j] = True
                check(i,j)

# 빙고 확인 함수
def check(x,y) :
    global result
    
    for i in range(4) :
        if result == 3 :
            return result
        
        cnt = 1
        
        for j in range(1,5) :
            nx = x + dx[i] * j
            ny = y + dy[i] * j
            if 0 <= nx < 5 and 0 <= ny < 5 :
                if visited[nx][ny] :
                    cnt += 1
                    
        for j in range(1,5) :
            nx = x + dx[i] * (-1) * j
            ny = y + dy[i] * (-1) * j
            if 0 <= nx < 5 and 0 <= ny < 5 :
                if visited[nx][ny] :
                    cnt += 1
                    
        if cnt == 5 :
            result += 1

result = 0
number_count = 0
result_arr = []

# 사회자가 부르는 숫자 리스트 * 5
for _ in range(5) :
    number = list(map(int,input().split()))
# 숫자 리스트 한개씩 순회 후 방문 처리 
    for i in range(5) :
        number_count += 1
        bingo(number[i])
        if result == 3 :
            result_arr.append(number_count)

print(result_arr[0])
    
# 31120	32