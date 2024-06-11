n = int(input())
card = list(map(int,input().split()))
d = [1] * (n+1)

for i in range(n) :
  for j in range(i) :
    if card[i] > card[j] :
      d[i] = max(d[i],d[j]+1)

print(max(d))

