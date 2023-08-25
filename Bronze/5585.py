import sys
input = sys.stdin.readline
yen = [500,100,50,10,5,1]
N = int(input())
cnt = 0
change = 1000 - N
for i in yen :
  cnt += change // i 
  change %= i

print(cnt)
  