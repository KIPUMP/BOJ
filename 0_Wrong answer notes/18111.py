# https://www.acmicpc.net/problem/18111
import sys
input = sys.stdin.readline

                            
n,m,b = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

time = [0 for i in range(257)]

height = 0
for g in range(257) :
    block = b 
    for i in arr :
        if i <= g :
            time[g] += g - i
            block -= g -i
        else :
            time[g] += 2 * (i - g) 
            block += i - g
    if block >= 0 and time[g] <= time[height] :
        height = g

print(time[height],height)


