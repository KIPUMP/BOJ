n = int(input())
charactor = 666
cnt = 0
while True :
  if '666' in str(charactor) :
    cnt += 1
  if cnt == n :
    print(charactor)
    break
  charactor += 1
