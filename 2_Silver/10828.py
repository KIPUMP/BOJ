import sys
N = int(sys.stdin.readline())
stack = []

for _ in range(N) :
  x = list(sys.stdin.readline().split())
  if x[0] == "push" :
    stack.append(x[1])
  elif x[0]  == "pop" :
    if len(stack) == 0 :
      print(-1)
    else :
      v = stack.pop()
      print(v)
  elif x[0]  == "size" :
    print(len(stack))
  elif x[0]  == "empty" :
    if len(stack) == 0 :
      print(1)
    else :
      print(0)
  elif x[0] == "top" :
    if len(stack) == 0 :
      print(-1) 
    else:
      print(stack[-1])
