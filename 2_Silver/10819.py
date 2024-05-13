from itertools import permutations

n = int(input())

arr = list(map(int,input().split()))

result = []
for i in permutations(arr,n) :
  sum_val = 0
  for j in range(n-1) :
    sum_val += abs(i[j] - i[j+1])

  result.append(sum_val)

print(max(result))

