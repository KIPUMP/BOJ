from collections import Counter
t = int(input())

for i in range(t) :
  n = int(input())
  cloth = []
  for j in range(n) :
    a,b = input().split()
    cloth.append(b)
  
  cloth_Counter = Counter(cloth)
  cnt = 1

  for i in cloth_Counter :
    cnt *= cloth_Counter[i] + 1

  print(cnt-1)
  