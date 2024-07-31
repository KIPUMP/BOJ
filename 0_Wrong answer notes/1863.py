# 코딩테스트 2주차
# https://www.acmicpc.net/problem/1863
# 이전 점보다 y값이 작아지는 지점에서 건물을 세어주면 된다. 
import sys
input = sys.stdin.readline

n = int(input())
skylines = []
for i in range(n) :
    x,y = map(int,input().split())
    skylines.append(y)                      # 건물의 높이 삽입
skylines.append(0)                          


stack = [0]                                 # 스택이 비는 걸 방지하기 위한 0 초기화
result = 0
for p in skylines :
    height = p 
    while stack[-1] > p :
        if stack[-1] != height :
            result += 1
            height = stack[-1]
        stack.pop()
    stack.append(p)
print(result)

# 31120	52
