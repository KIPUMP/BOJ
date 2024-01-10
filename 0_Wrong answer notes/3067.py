import sys
input = sys.stdin.readline

for _ in range(int(input())) :      # 테스트 케이스 개수
    n = int(input())                # 동전의 개수
    coins = list(map(int,input().split()))      
    m = int(input())                # 목표 금액
    d = [0] * (m+1)                 
    d[0] = 1                        # 0원을 만드는 방법 = 1가지(동전을 쓰지 않음)
    
    for i in range(n) :             # 각 동전 단위를 반복      
        for j in range(coins[i],m+1) :      # 각 동전 금액에서 목표 금액까지 각 금액을 반복
            d[j] += d[j - coins[i]]         
            
    print(d[m])
            
            
    