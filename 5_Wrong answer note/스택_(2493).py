# https://www.acmicpc.net/problem/2493
n = int(input())
arr = list(map(int,input().split()))

stack = []
result = [0] * n
for i in range(n) :
    while stack :
        if stack[-1][1] > arr[i] :
            result[i] = stack[-1][0]
            break
        else :
            stack.pop()
    stack.append((i+1,arr[i]))      # 순서와 높이를 stack에 넣는다 
    
print(*result)

# 114664	540