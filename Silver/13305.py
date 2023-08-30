import sys
input = sys.stdin.readline
N = int(input())
road = list(map(int,input().split()))
station = list(map(int,input().split()))
money = station[0] * road[0]
m = station[0]
dist = 0
for i in range(1,N-1) :
  if station[i] < m :
    money += m * dist
    dist = road[i]
    m = cost[i]
  else :
    dist += road[i]
  
  if i == N-2 :
    money += m * dist

print(money)




