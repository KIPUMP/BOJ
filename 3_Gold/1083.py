#  https://www.acmicpc.net/problem/1083
import sys
input = sys.stdin.readline

def greedy_sort(arr,start,cnt) :                # x 범위에서 가장 큰수 를 앞으로 끌어와야 한다
    while start < n and cnt > 0 :
        max_idx = start
        
        for i in range(start,min(n-1,start+cnt)+1) :    
            if arr[max_idx] < arr[i] :
                max_idx = i
        for i in range(max_idx,start,-1) :
            arr[i], arr[i-1] = arr[i-1], arr[i]
            cnt -= 1
        
        start += 1
    
    return arr
        

n = int(input())
arr = list(map(int,input().split()))
s = int(input())

arr = greedy_sort(arr,0,s)

print(*arr)
                
                
# 31120	32
        
