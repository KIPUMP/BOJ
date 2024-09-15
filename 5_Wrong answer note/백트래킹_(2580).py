# https://www.acmicpc.net/problem/2580
# https://chaeyami.tistory.com/224 - 풀이 참고
# 백트래킹 - 스도쿠 
import sys
 
SIZE = 9
 
sudoku = [list(map(int,sys.stdin.readline().split())) for _ in range(SIZE)] # 스도쿠 문제
blank_coord = [(i, j) for i in range(SIZE) for j in range(SIZE) if sudoku[i][j] == 0] # 빈칸의 좌표를 나타낸 리스트
 
def check(y, x, check_num):
    BOX_SIZE = 3
    
    for i in range(SIZE): # 가로, 세로 체크
        if sudoku[y][i] == check_num or sudoku[i][x] == check_num:
            return False
    
    for i in range(BOX_SIZE): # 3x3영역 체크
        for j in range(BOX_SIZE):
            if sudoku[y // BOX_SIZE * BOX_SIZE + i][x // BOX_SIZE * BOX_SIZE + j] == check_num:
                return False
    return True
 
def dfs(n):
    if n == len(blank_coord):
        for i in sudoku: 
            print(*i) 
        exit() 
    
    for check_num in range(1,10):
        y, x = blank_coord[n]
        # y = blank_coord[n][0]
        # x = blank_coord[n][1]
        if check(y, x, check_num):
            sudoku[y][x] = check_num
            dfs(n+1)
            sudoku[y][x] = 0
            
dfs(0)

