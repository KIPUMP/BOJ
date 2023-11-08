import sys
input = sys.stdin.readline
n,x = map(int,input().split())
visit = list(map(int,input().split()))

d = [0] * (n+1)
d[0] = 0
tmp = sum(visit[:x])

max_val = tmp
cnt = 1
for i in range(x,n) :
    
    tmp -= visit[i-x]
    tmp += visit[i]
    
    if max_val < tmp :
        max_val = tmp
        cnt = 1
        
    elif max_val == tmp :
        cnt += 1
        

if max_val == 0 :
    print("SAD")
else :
    print(max_val)
    print(cnt) 