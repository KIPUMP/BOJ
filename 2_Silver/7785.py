n = int(input())
log = set()

for i in range(n) :
  name, work = input().split()

  if work == 'enter' :
    log.add(name)

  elif work == 'leave' :
    log.discard(name)


log = sorted(log,reverse=True)
for i in log :
  print(i)