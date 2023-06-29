n = int(input())
cnt = 0
x = n
while True :
  cnt+=1
  a = x // 10
  b = x % 10
  c = (a+b) % 10

  x = (b * 10) + c

  if x == n :
    print(cnt)
    break


