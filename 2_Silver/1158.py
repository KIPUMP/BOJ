from collections import deque
n,k = map(int,input().split())
queue = deque()
result = []

for i in range(1,n+1) :
  queue.append(i)

while queue :
  for _ in range(k-1) :
    queue.append(queue.popleft())
  
  x = queue.popleft()
  result.append(x)

print(str(result).replace('[','<').replace(']','>'))
  