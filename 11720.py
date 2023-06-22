sum_val = 0
n = int(input())
num = int(input())

for _ in range(n) :
  sum_val += num % 10

  num //= 10

print(sum_val)
