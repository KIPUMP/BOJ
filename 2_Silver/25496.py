# https://www.acmicpc.net/problem/25496

p,n  = map(int,input().split())         # 피로도, 장신구 개수 
arr = list(map(int,input().split()))    # 장신구

arr.sort()

result =  0
for i in range(n) :
    if p < 200 :
        result += 1
        p += arr[i]
    
print(result)

# 31120	32