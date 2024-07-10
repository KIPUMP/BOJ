import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
arr = sorted(map(int,input().split()))

distance = []

if k >= n :
    print(0)
    sys.exit(0)    

for i in range(1,n) :
    distance.append(arr[i]-arr[i-1])
    
for i in range(k-1) :
    distance.remove(max(distance))
    
    
print(sum(distance))