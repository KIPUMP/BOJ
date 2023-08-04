coin = [25 , 10 , 5 , 1]

for _ in range(int(input())) :
  C = int(input())
  change = []
  for i in coin :
    change.append(C//i)
    C %= i
  
  for i in change :
    print(i,end=" ")