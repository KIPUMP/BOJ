import sys
input = sys.stdin.readline

for _ in range(int(input())) :
  result = 0
  n = int(input())
  stock = list(map(int,input().split()))  
  max = 0

  for i in range(len(stock) -1, -1, -1) :
    if stock[i] > max :
      max = stock[i]
    else :
      result += max - stock[i]

  print(result)



    

      
      
    
    

  

