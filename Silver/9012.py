import sys
T = int(sys.stdin.readline())

for _ in range(T) :
  VPS = input()
  arr = list(VPS)
  
  while len(arr) > 2 :
    if arr[0] == ")" :
      break

    else :
      arr.remove("(")
      for i in arr :
        if i == ")" :
          arr.remove(")")
          break

  if arr == ["(",")"] :
    print("YES")
  else : 
    print("NO")
    

    

        