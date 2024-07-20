#https://www.acmicpc.net/problem/24416

n = int(input())

def fib(n) :
    a,b = 1,1
    for _ in range(3,n+1) :
        a,b = b,a+b                 
    '''
    f(1) = 1
    f(2) = 1
    f(3) = 1 + f(2) = 2
    f(4) = 2 + f(3)
    '''
    return b

def fibonacci(n) :
    return n-2

print(fib(n), fibonacci(n))