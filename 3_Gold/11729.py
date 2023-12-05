import sys
sys.setrecursionlimit(10**6)
n = int(input())
cnt = 0
result = []
def hanoi(n,start,mid,end) :
    global cnt,result
    if n == 1 :
        cnt += 1
        result.append((start,end))
    else :
        hanoi(n-1,start,end,mid)
        hanoi(1,start,mid,end)
        hanoi(n-1,mid,start,end)
        

hanoi(n,1,2,3)
print(cnt)
for i in result :
    print(*i)
    