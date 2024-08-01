# 코딩테스트 2주차
# https://www.acmicpc.net/problem/1863
# 이전 점보다 y값이 작아지는 지점에서 건물을 세어주면 된다. 
import sys
input = sys.stdin.readline

n = int(input())
skylines = []
for _ in range(n):
    x, y = map(int, input().split())
    skylines.append(y)

skylines.append(0)  # 마지막 스택 처리를 위한 0 추가

stack = [0]
result = 0

for height in skylines:
    p = height
    while stack[-1] > p:
        if stack[-1] != height:
            result += 1
        stack.pop()
    stack.append(height)

print(result)
