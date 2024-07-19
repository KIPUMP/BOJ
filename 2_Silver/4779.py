# https://www.acmicpc.net/problem/4779

def sol(n) :
    if n == 0 :
        return ['-']
    return sol(n-1) + [' '] * len(sol(n-1)) + sol(n-1)

while True :
    try :
        n = int(input())
        print(*sol(n))
        
    except : 
        break
