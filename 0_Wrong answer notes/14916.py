# https://www.acmicpc.net/problem/14916
# ex. n = 13 → 2원 - 4개, 5원 1개로 최소 완성(무조건 탐욕 X)

n = int(input())

count = 0
while n > 1 :
    if n % 5 == 0 :                 # 5로 나누어 떨어지면 남은 동전을 5원으로 바꾼다
        count += (n//5)
        n %= 5
        
    else :                          # 2원 짜리를 한개씩 빼면서 비교
        count += 1
        n -= 2
        
if n == 0 :
    print(count)
else :
    print(-1)
    
# 31120	36
