import sys
input = sys.stdin.readline
n,m = map(int,input().split())
score = []
cnt = 0
for _ in range(n) :
    p,l = map(int,input().split())
    grade = sorted(map(int,input().split()))
    if p < l :
        score.append(1)
    else :
        score.append(grade[p-l])
        
score.sort()

for i in score :
    if i > m :
        break
    cnt += 1
    m -= i
    
print(cnt)