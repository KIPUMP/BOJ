# https://www.acmicpc.net/problem/9934
import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

dx = [0,-1,0,1]
dy = [-1,0,1,0]

result = set()                                  # 중복을 피하기 위한 set
def dfs(x,y) :                                  # dfs 기반 백트래킹
    
    global number
    number.append(arr[x][y])
    if len(number) == 6 :
        num = 0
        for i in range(6) :
            num += number[i] * (10**(5-i))
        result.add(num)
        return 
        
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5 :
            dfs(nx,ny)
            number.pop()
            
            
arr = [list(map(int,input().split())) for _ in range(5)]

for i in range(5) :
    for j in range(5) :
        number = []
        dfs(i,j)
    
print(len(result))

#  31632	56
