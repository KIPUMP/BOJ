n = int(input())
left,right = 0,0
cnt = 0
total = 0
while right <= n and left <= right :
  if total == n :
    cnt += 1
    right += 1
    total += right

  elif total < n :
    right += 1
    total += right

  else :
    total -= left
    left += 1
    
print(cnt) 