# https://www.acmicpc.net/problem/2740
# 문제 해결 : 구현 , 문제 이해(배열의 곱)
# (n,m) * (m,k) = (n*k)

n,m = map(int,input().split())
arr_1 = [list(map(int,input().split())) for _ in range(n)]
m,k = map(int,input().split())
arr_2 =[list(map(int,input().split())) for _ in range(m)]

result_arr = [[0] * k for _ in range(n)]


for i in range(n) :
  for j in range(k) :
    for l in range(m) :
      result_arr[i][j] += arr_1[i][l] * arr_2[l][j]
      

for i in range(n) :
  print(*result_arr[i])