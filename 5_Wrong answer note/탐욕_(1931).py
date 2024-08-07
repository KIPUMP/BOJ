# https://www.acmicpc.net/problem/1931
import sys
input = sys.stdin.readline

n = int(input())
meetings = []

for _ in range(n) :
    start,end = map(int,input().split())
    meetings.append([start,end])
    
meetings = sorted(meetings,key = lambda x : (x[1],x[0]))        # 종료시간 기준으로 오름차순

count = 0
last_end_time = 0

for start,end in meetings :
    if start >= last_end_time :
        count += 1
        last_end_time = end

print(count)
