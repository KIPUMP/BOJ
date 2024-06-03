n = int(input())
result = 0 

if n == 1 or n == 3 :
  print(-1)

else :
  
  result += n // 5
  n %= 5

  while True :
    if n % 2 != 0 : 
      result -= 1
      n += 5
    else :
      result += n // 2
      print(result)
      break
    


