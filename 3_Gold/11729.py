arr = []
cnt = 0
def hanoi(n,start,mid,end) :
    global cnt
    if n == 1:
        cnt+=1
        arr.append((start,end))
        
        return
    
    else :
        hanoi(n-1,start,end,mid)
        hanoi(1,start,mid,end)
        hanoi(n-1,mid,start,end)
        
n = int(input())

hanoi(3,1,2,3)
print(cnt)
for i in arr :
    print(*i)
    
