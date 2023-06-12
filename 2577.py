arr_count = [0,0,0,0,0,0,0,0,0,0]

prod = 1

for i in range(3) :
  i = int(input())
  prod *= i


while True:
  n = prod % 10 
  
  for i in range(0,10) :
    if n == i :
      arr_count[i] += 1
  
  if prod < 10 :
    break
  else :
    prod //= 10



for i in arr_count :
  print(i)




