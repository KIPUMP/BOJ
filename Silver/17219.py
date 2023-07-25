import sys
input = sys.stdin.readline

N, M = map(int, input().split())
add = dict()

for _ in range(N) :
  site,ps = input().split()
  add[site] = ps

for _ in range(M) :
  address = input().rstrip()
  print(add[address])