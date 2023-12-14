s = list(input().rstrip())
blanket = False
result = ''
stack = []
for i in s :
  if i == '<' :
    blanket = True
    for _ in range(len(stack)) :
      result += stack.pop()
  stack.append(i)

  if i == '>' :
    blanket = False 
    for _ in range(len(stack)) :
      result += stack.pop(0)

  if i == ' ' and not blanket :
    stack.pop()
    for _ in range(len(stack)) :
      result += stack.pop()
    result += ' '
    
for _ in range(len(stack)) :
  result += stack.pop()

print(result)