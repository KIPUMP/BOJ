# https://www.acmicpc.net/problem/2167
# 해결 : 부분합 , 문제 이해
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
d = [[0] * (m+1) for _ in range(n+1)]

for i in range(1,n+1) :
    for j in range(1,m+1) :
        d[i][j] = d[i-1][j] + d[i][j-1] - d[i-1][j-1] + arr[i-1][j-1]          # 점화식(배열 합)
        
        '''                     0   0      0      0
        1 + 2  +  4           
                                0 [[1]]   [3]    7
        +   +     +       →                 
        8 +[16] + 32            0  [9]    27     63
        
        '''

        

k = int(input())
for _ in range(k) :
    x1,y1,x2,y2 = map(int,input().split())
    result = d[x2][y2] - d[x1-1][y2] - d[x2][y1-1] + d[x1-1][y1-1]            # 점화식(배열 차)
    '''
    [[1]]  3]  7
    
    [9]    27  63
    '''
    print(result)
    
    
    