n,m = map(int,input().split())
trees = list(map(int,input().split()))
left,right = 0, max(trees)
mid = (left + right) // 2

def get_tree(h) :
  result = 0
  for t in trees :
    if t > h :
      result += t - h
  return result

result = 0
while left <= right :
  if get_tree(mid) >= m :
    result = mid
    left = mid + 1

  else :
    right = mid - 1
  
  mid = (left + right) // 2

print(result)
  

    
