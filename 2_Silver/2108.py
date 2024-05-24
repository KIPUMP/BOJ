import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
result = []
arr.sort()

result.append(sum(arr) // n)
result.append(arr[(n//2)])

max_count =  {}
for i in range(n) :
  max_count[arr[i]] = arr.count(arr[i])

max_count_num = arr[0]

for i in max_count.keys :
  if max_count[max_count_num] < max_count[i] :
    max_count_num = i


result.append(max_count_num)


result.append(max(arr) - min(arr))

for i in range(4) :
  print(result[i])


