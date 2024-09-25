# https://www.acmicpc.net/problem/31848

n = int(input())
hole = list(map(int,input().split()))
q = int(input())
acorn = list(map(int,input().split()))

result = []
for i in range(q) :
    acorn_size = acorn[i]
    for j in range(n) :
        if acorn_size <= hole[j] :
            result.append(i+1)
            break
        else :
            acorn_size -= 1
    
print(*result)

