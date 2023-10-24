import sys
input = sys.stdin.readline
n,m = map(int,input().split())
d = [0] * 100001
square = []
dot = []

for _ in range(m) :
    dot.append(list(map(int,input().split())))
    
for i in range(n) :
    square.append(list(map(int,input().split())))
tmp = 0
d[0] = square[0][0]
for i in range(len(d)) :
    for j in range(n) :
        tmp += square[i%n][j]
        d[i][j] = tmp
        
for i in range(m) :
    # print(d[dot[i][0]][dot[i][1]] - d[dot[i][2]][dot[i][3]])
    print(d[dot[i][0]][dot[i][1]] - d[dot[i][2]][dot[i][3]])
    
            