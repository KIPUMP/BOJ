import sys
input = sys.stdin.readline
n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
d = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        d[i][j] = d[i-1][j] + d[i][j-1] - d[i-1][j-1] + arr[i-1][j-1]

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    result = d[x][y] - d[i-1][y] - d[x][j-1] + d[i-1][j-1]
    print(result)
