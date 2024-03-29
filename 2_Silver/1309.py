
n = int(input())
d = [1 for _ in range(n+1)]

d[1] = 3
d[2] = 7

if n == 1 :
  print(d[n])


else :
  for i in range(3,n+1) :
    d[i] = (2 * d[i-1] + d[i-2]) % 9901

  print(d[n])  