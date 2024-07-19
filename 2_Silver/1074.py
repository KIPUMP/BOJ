# https://www.acmicpc.net/problem/1074
# 사각형을 쪼개는 방식으로 계산
import sys
sys.setrecursionlimit(10**6)

n,t,c = map(int,input().split())
def solution(n,t,c) :
    if n == 0 :
        return  0 
    return  2*(t%2)+(c%2) + 4*(solution(n - 1,t // 2,c // 2))       

print(solution(n,t,c))