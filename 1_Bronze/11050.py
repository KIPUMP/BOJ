def bino_ceof(n,k):
  if k == 0 or n == k :
    return 1
  return bino_ceof(n-1,k) + bino_ceof(n-1,k-1)

n,k = map(int,input().split())

print(bino_ceof(n,k))