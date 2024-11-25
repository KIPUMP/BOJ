# https://www.acmicpc.net/problem/20044
import sys

input = sys.stdin.readline

n = int(input())
arr = sorted(map(int,input().split()))

team_rate = arr[0] + arr[-1]

for i in range(1,n) :
    sum_val = arr[i] + arr[-(i+1)]
    if sum_val < team_rate :
        team_rate = sum_val
        
print(team_rate)

# 32140	44