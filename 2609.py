def GCD(n,m) :
  if m == 0  :
    return n 
  else :
    return GCD(m,n%m)

def LCM(n,m) :
  return (n*m) // GCD(n,m) 

n,m = map(int,input().split())

print(GCD(n,m))
print(LCM(n,m))