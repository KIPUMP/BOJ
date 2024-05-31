x_dot = []
y_dot = []
result_dot = []
for _ in range(3) :
  x,y = map(int,input().split())
  x_dot.append(x)
  y_dot.append(y)

if x_dot[0] == x_dot[1] and x_dot[0] != x_dot[2] :
  result_dot.append(x_dot[2])
elif x_dot[0] != x_dot[1] and x_dot[0] == x_dot[2] :
  result_dot.append(x_dot[1])
elif x_dot[1] == x_dot[2] and x_dot[0] != x_dot[1] :
  result_dot.append(x_dot[0])

if y_dot[0] == y_dot[1] and y_dot[0] != y_dot[2] :
  result_dot.append(y_dot[2])
elif y_dot[0] != y_dot[1] and y_dot[0] == y_dot[2] :
  result_dot.append(y_dot[1])
elif y_dot[1] == y_dot[2] and y_dot[0] != y_dot[1] :
  result_dot.append(y_dot[0])

print(*result_dot)



