import sys
S = set()
n = int(sys.stdin.readline())

for _ in range(n) :
  tmp = sys.stdin.readline().strip().split()
  if len(tmp) == 1 :
    command = tmp[0]
  else :
    command,target = tmp[0],tmp[1]
    target = int(target)
  
  if command == "add" :
    S.add(target)
  elif command == "check" :
    print(1 if target in S  else 0)
  
  elif command == "remove" :
    S.discard(target)
  elif command == "toggle" :
    if target in S :
      S.discard(target)
    else :
      S.add(target)
  elif command == "all" :
    S = set([i for i in range(1,21)])
  else :
    S = set()
    
