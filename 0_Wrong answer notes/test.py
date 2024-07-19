import sys
sys.setrecursionlimit(10**6)

# def f(n) :
#     if n == 1 :                     # 종료 조건
#         return 1
#     return f(n-1) + n               # 재귀 점화식

# n = int(input())

# print(f(n))    


def fibo(n) :
    
    return 1 if n <= 2 else fibo(n-1) + fibo(n-2)
    
n = int(input())
print(fibo(n))
    