arr_number = []
arr_left = []
for _ in range(10) :
  n = int(input())
  arr_number.append(n)
  arr_left.append(n%42)

cnt = 0
for i in arr_left :
  cnt +=1
  if arr_left.count(i) > 1 :
    cnt -= 1
  
    

print(cnt)
  