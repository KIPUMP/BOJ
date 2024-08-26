# https://www.acmicpc.net/problem/23971
# h행 w열의 크기의 테이블에 모든 참가자가 세로 n칸 or가로 m칸
# 거리 두기를 한다는 가정하에, 최대 수용자를 구하는 문제
import math
h,w,n,m = map(int,input().split())

print(math.ceil(h / (n+1)) * math.ceil(w / (m+1)))

