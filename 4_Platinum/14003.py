import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

def binary_search(arr,target) :
  low = -1
  high = len(arr)

  while low + 1 < high :
    mid = (low + high) // 2
    if target > arr[mid] :
      low = mid
    else :
      high = mid

  return high

result = [-1000000001]
total =  [(-1000000001,0)]

arr = arr[::-1]

while arr :
  x = arr.pop()

  if x > result[-1] :
    total.append((x,len(result)))
    result.append(x)

  else :
    idx = binary_search(result,x)
    result[idx] = x
    total.append((x,idx))

lis_length = len(result)-1
lis = []

#print(lis_total)

while total and lis_length:
    num, idx = total.pop()
    if idx == lis_length:
        lis.append(num)
        lis_length -= 1

print(len(lis))
print(*lis[::-1])
