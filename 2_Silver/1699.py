n = int(input())
d = [i for i in range(n+1)]

for i in range(1,n+1) :
<<<<<<< HEAD
  for j in range(1,i) :
    if j**2 > i :
      break
    else : 
      if d[i] > d[i-(j**2)] + 1 :
        d[i] = d[i-(j**2)] + 1

=======
    for j in range(1,i) :
        if j**2 > i :
            break
        else :
            if d[i] > d[i - (j**2)] + 1:
                d[i] = d[i - (j**2)] + 1
                
>>>>>>> c6bc2d5c658d90977e7b7d74d44755329f187c0e
print(d[n])