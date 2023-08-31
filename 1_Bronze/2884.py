h,m = map(int,input().split())

m -= 45
if h > 0 :
  if m < 0 :
    h -= 1 
    m = 60 + m
else :
  if m < 0 :
    h = 23
    m = 60 + m




print(h,m)

