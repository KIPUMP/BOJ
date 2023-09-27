result = []
n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
def dfs(v) :
    if len(result) == m :
        print(*result)
        return
    for i in range(v,n) :
        result.append(arr[i])
        dfs(i)
        result.pop()
        
dfs(0)