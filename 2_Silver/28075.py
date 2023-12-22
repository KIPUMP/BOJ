n,m = map(int,input().split())
work = [list(map(int,input().split())) for _ in range(2)]
result = 0

def solution(n,m,idx) :
  global result
  if n == 0 :
    if m <= 0 :
      result += 1
    return        # 재귀 알고리즘 구현시 재귀 호출의 마침을 알리기 위한 return 
  
  for i in range(2) :
    for j in range(3) :
      if idx == j :
        solution(n-1,m-work[i][j]/2,j)
      else :
        solution(n-1,m-work[i][j],j)
        

solution(n,m,-1)
print(result)
