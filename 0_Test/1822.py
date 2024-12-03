# https://www.acmicpc.net/problem/1822
# 풀이 참고 : https://ji-gwang.tistory.com/305
import sys

nA,nB = map(int,input().split())

A = set(map(int,input().split()))
B = set(map(int,input().split()))

print(len(A-B))
print(*sorted(list(A-B)))


# 146304	1000