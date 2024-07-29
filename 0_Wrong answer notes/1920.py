import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def binary_search(arr,target,start,end) :           # (정렬된) 리스트, 찾을 값, 처음 인덱스 , 끝 인덱스
    if start > end :
        return False
    else :
        mid = (start + end) // 2
        
        if arr[mid] == target :
            return arr[mid]
        
        elif arr[mid] < target :
            return binary_search(arr,target,mid+1,end)
        
        else :
            return binary_search(arr,target,start,mid-1)

n = int(input())
arr_1 = sorted(map(int,input().split()))
m = int(input())
arr_2 = list(map(int,input().split()))


for i in range(m) : 
    if binary_search(arr_1,arr_2[i],0,n-1):
        print(1)
    else :
        print(0)
    
    




