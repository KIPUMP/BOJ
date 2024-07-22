# https://www.acmicpc.net/problem/15650
# 해법 : 백트래킹
# from itertools import combinations → 사용 시 n,m의 크기에 따라 시간 초과 날 수 있음
n,m = map(int,input().split())
visited = [False] *(n+1)

result = []

def solution(start) :
    if len(result) == m :
        print(*result)
        return
    else :
        for i in range(start,n+1) :                 # 하기 위해 start 변수 추가
            if visited[i] :
                continue
            else :
                visited[i] = True
                result.append(i)
                solution(i+1)           
                visited[i] = False
                result.pop()
                    
solution(1)

# 31120	40