import sys
sys.setrecursionlimit(10**6)

r,c = map(int,input().split())
arr = [list(input().rstrip()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
dx = [0,1,-1,0]
dy = [1,0,0,-1]

def dfs(x,y) :
  global v_cnt,o_cnt
  visited[x][y] = True
  for i in range(4) :
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < r and 0 <= ny < c :
      if arr[nx][ny] == '.' and visited[nx][ny] == False :
        visited[nx][ny] = True
        dfs(nx,ny)
      elif arr[nx][ny] == 'o' and visited[nx][ny] == False :
        visited[nx][ny] = True
        dfs(nx,ny)
        o_cnt += 1
      elif arr[nx][ny] == 'v' and visited[nx][ny] == False :
        visited[nx][ny] = True
        dfs(nx,ny)
        v_cnt += 1

total_v_cnt = 0
total_o_cnt = 0

for i in range(r) :
  for j in range(c) :
    if visited[i][j] == False :
      if arr[i][j] == 'v':
        v_cnt = 1
        o_cnt = 0
        dfs(i,j)
        if v_cnt >= o_cnt :
          total_v_cnt += v_cnt
        else :
          total_o_cnt += o_cnt
      elif arr[i][j] == 'o' :
        v_cnt = 0
        o_cnt = 1
        dfs(i,j)
        if v_cnt >= o_cnt :
          total_v_cnt += v_cnt
        else :
          total_o_cnt += o_cnt

print(total_o_cnt,total_v_cnt)      


