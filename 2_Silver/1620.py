import sys
N,M = map(int,sys.stdin.readline().split())

dict = {}

for i in range(1,N+1) :
  a = sys.stdin.readline().rstrip()
  dict[i] = a
  dict[a] = i

for i in range(M) :
  quest = sys.stdin.readline().rstrip()
  if quest.isdigit() :
    print(dict[int(quest)])
  else :
    print(dict[quest])