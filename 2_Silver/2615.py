import sys
input = sys.stdin.readline

board = []
for i in range(19):
    board.append(list(map(int, input().split())))

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for i in range(19) :
    for j in range(19) :
        if board[i][j] != 0:
            focus = board[i][j]             # 흑, 백 판별
            for k in range(4) :
                cnt = 1                     # 방향 전환 할 때마다 1로 초기화
                nx = i + dx[k]
                ny = j + dy[k]
                
                while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == focus :
                    cnt += 1
                    if cnt == 5 :
                        if 0 <= i - dx[k] < 19 and 0 <= j - dy[k] < 19 :     # 6목 체크
                            if board[i- dx[k]][j - dy[k]] == focus :
                                break
                        
                        if 0 <= nx + dx[k] < 19 and 0 <= ny + dy[k] < 19 :   # 6목 체크
                            if board[nx + dx[k]][ny + dy[k]] == focus :
                                break
                            
                        print(focus)
                        print(i+1,j+1)
                        sys.exit()
                        
                    nx += dx[k]             # x 좌표 이동
                    ny += dy[k]             # y 좌표 이동
                
print(0)
            
    

