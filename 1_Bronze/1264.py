arr = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']

while True :
  word = input()
  cnt = 0
  if word == '#' :
    break
  for i in word :
    for j in arr :
      if i == j :
        cnt += 1
  
  print(cnt)
  

  