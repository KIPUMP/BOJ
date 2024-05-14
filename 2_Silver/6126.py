v,n = map(int,input().split())

coins = [int(input()) for _ in range(v)] 

d = [0] * (n+1)

for i in range(v) :
  d[coins[i]] = 1