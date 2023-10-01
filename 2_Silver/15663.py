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
    remember = 0
    for i in range(n) :
        if visited[i] == False and remember != arr[i] :
            visited[i] = True
            result.append(arr[i])
            remember = arr[i]
            dfs()
            visited[i] = False
            result.pop()
            
dfs()

            
