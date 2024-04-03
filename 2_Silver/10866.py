from collections import deque
import sys
input = sys.stdin.readline
arr = deque()

for _ in range(int(input())) :
  order = list(input().split()) 

  if order[0] == "push_front" :
    arr.appendleft(order[1])

  elif order[0] == "push_back":
    arr.append(order[1])
      
  elif order[0] == "pop_front" :
    if len(arr) == 0:
      print(-1)
    else :
      print(arr.popleft())

  elif order[0] == "pop_back" :
    if len(arr) == 0:
      print(-1)
    else :
      print(arr.pop())
  elif order[0] == "size" :
    print(len(arr))

  elif order[0] == "empty" :
    if len(arr) == 0 :
      print(1)
    else :
      print(0)

  elif order[0] == "front" :
    if len(arr) == 0:
      print(-1)
    else :
      print(arr[0])

  elif order[0] == "back" :
    if len(arr) == 0 :
      print(-1)
    else :
      print(arr[-1])





