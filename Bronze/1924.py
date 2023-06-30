arr_2007 =  [0,31,28,31,30,31,30,31,31,30,31,30,31]
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
x,y = map(int,input().split())
a,b = 1,1
cnt = 1

while True :
  if x == a and y == b :
    break  
  b += 1
  cnt += 1
  if arr_2007[a] < b :
    b = 1
    a += 1

if cnt > 6 :
  cnt %= 7
  
print(day[cnt])

