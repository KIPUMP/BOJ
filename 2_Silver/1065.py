n = int(input())
cnt = 0

for i in range(1,n+1):
  x = str(i)
  if len(x) <= 2 :
    cnt += 1
  else :
    gap = []
    for j in range(len(x)-1) :
      gap.append(int(x[j+1]) - int(x[j]))
    ok = True
    for j in range(len(gap)-1) :
      if gap[j+1] != gap[j] :
        ok = False
        break
    if ok:
      cnt += 1

print(cnt)
