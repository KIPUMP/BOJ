n = int(input())
log = dict()


for i in range(n) :
  name, work = input().split()

  if work == 'enter' :
    log[name] = True

  elif work == 'leave' :
    del log[name]

log = sorted(log, reverse=True)

for i in log :
  print(i)