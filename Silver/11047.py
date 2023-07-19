N,K = map(int,input().split())
coin = []
for _ in range(N) :
  coin.append(int(input()))

coin.sort()
coin.reverse()
cnt = 0
for i in coin :
  if i > K :
    continue
  cnt += (K // i)
  K %= i

  if K == 0 :
    break

print(cnt)

  