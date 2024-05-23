from itertools import product
import sys
input = sys.stdin.readline

t = int(input())
for i in range(t) : 
    n,k = map(int,input().split())
    arr = sorted(map(int,input().split()))
    result = []
    for j in product(arr,repeat=2) :
        result.append(j)
        
    result = sorted(result,key = lambda x : (x[0],x[1]))
    
    print(f"#{i+1} {sum(result[k-1])}")
    
    
    
        

    
