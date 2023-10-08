import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    coin = list(map(int,input().split())) 
    m = int(input())
    d = [0] * (m+1)
    d[0] = 1
    for i in range(n) :
      for j in range(coin[i],m+1) :
        d[j] += d[j - coin[i]]    
    
    print(d[m])