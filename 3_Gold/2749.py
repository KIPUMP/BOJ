import sys

n = int(input())

d = [0] * (n+1)

if n <= 1 :
    d[n] = n 
    print(d[n] % 1000000)
    sys.exit(0)
    
else :
    d[1] = 1
    for i in range(2,n+1) :
        d[i] = d[i-2] + d[i-1]
        
print(d[n] % 1000000)
    


        