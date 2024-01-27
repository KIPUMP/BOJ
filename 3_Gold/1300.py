n = int(input())
k = int(input())
arr = [[0] * n for _ in range(n)]

for i in range(n) :
    for j in range(n) :
        arr[i][j] = i * j
        
