import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr = sorted(arr,reverse=True)

result = []
for i in range(n) :
  result.append(arr[i] + 1 + i)

print(max(result) + 1)

