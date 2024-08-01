# https://www.acmicpc.net/problem/25206
# 학점 계산 , P인 과목을 계산에서 뺀다

sum_val = 0
cnt = 0

for _ in range(20) :
    subject,grade,cost = input().split()
    cnt += float(grade)
    if cost == 'P' :
        cnt -= float(grade)
        continue
    elif cost == 'A+' :
        cost = 4.5
    elif cost =='A0' :
        cost = 4.0
    elif cost =='B+' :
        cost = 3.5
    elif cost =='B0' :
        cost = 3.0
    elif cost =='C+' :
        cost = 2.5
    elif cost =='C0' :
        cost = 2.0
    elif cost =='D+' :
        cost = 1.5
    elif cost == 'D0' :
        cost = 1.0  
    else :
        cost = 0
    sum_val += float(cost) * float(grade)

print(f"{sum_val / cnt:.6f}")
    
            