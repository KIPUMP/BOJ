import sys
candidate = []
n = int(input())
result = 0

for _ in range(n):
  candidate.append(int(input()))

if len(candidate) == 1 :
  print(result)
  sys.exit(0)


while candidate[0] <= max(candidate[1:]):
  for i in range(1,n) :
    if candidate[i] == max(candidate) :
      candidate[0] += 1
      candidate[i] -= 1
      result += 1      

print(result)