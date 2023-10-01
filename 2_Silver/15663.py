import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
arr = sorted(map(int,input().split()))
visited = [False] * n
result = []

def dfs() :
    # 길이가 m인지 확인 
    if len(result) == m :       
        print(*result)
        return
    # dfs 실시 
    for i in range(n) :
        if visited[i] == False :
            visited[i] = True
            result.append(arr[i])
            dfs()
            visited[i] = False
            result.pop()
            
dfs()

            
