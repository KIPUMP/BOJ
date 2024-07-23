# https://www.acmicpc.net/problem/15649
# 해법 : 백트래킹 : 모든 경우의 수를 탐색하는 대신 조건을 걸어서 유망하지 않은 경우에는 탐색을 중지하고 이전 노드로 돌아가서 다른 경우를 탐색한다
# from itertools import permutations  → 더 간단하지만 m이 커지면 시간 초과 날 수 있음
n,m = map(int,input().split())

visited = [False] * (n+1)             # 방문 관리
 
result = []                           

def solution() :
    if len(result) == m :               # 길이를 m으로 제한
        print(*result)
        return 
    else :
        for i in range(1,n+1) :
            if visited[i] :             # 이미 방문했다면 무시
                continue
            visited[i] = True           # 방문 표시
            result.append(i)            
            solution()                       # 재탐색
            visited[i] = False
            result.pop()
            
solution()


#31120	176