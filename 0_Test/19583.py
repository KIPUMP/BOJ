# https://www.acmicpc.net/problem/19583
import sys

input = sys.stdin.readline

s,e,q = input().split()

s = int(s[:2]) * 60 + int(s[3:])
e = int(e[:2]) * 60 + int(e[3:])
q = int(q[:2]) * 60 + int(q[3:])

res = set()
result = 0

while True :
    try:
        time,name = input().split()
        time = int(time[:2]) * 60 + int(time[3:])
        
        if time <= s :
            res.add(name)
            
        elif name in res :
            if e <= time <= q :
                res.remove(name)
                result += 1
    except :
        break    
    
print(result)

# 43412	144