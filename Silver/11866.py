N,K = map(int,input().split())
arr = [x for x in range(1,N+1)]
idx = 0
ans = []
for _ in range(N) :
  idx += K-1
  idx %= len(arr)
  ans.append(arr.pop(idx))

print(f"<{', '.join(map(str,ans))}>")

