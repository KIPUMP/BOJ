# https://www.acmicpc.net/problem/10815

# 이진 탐색 구현(리스트, 찾는 값, 첫 인덱스 , 끝 인덱스)
def binary_search(arr,target,start,end) :       
    if start > end :                      
        return 0
    else :
        mid = (start + end) // 2                        # 계속 중간을 탐색
        
        if arr[mid] == target :                         
            return 1                
        
        elif arr[mid] > target :
            return binary_search(arr,target,start,mid-1)       
        
        else :
            return binary_search(arr,target,mid+1,end)



n = int(input())
arr_1 = sorted(map(int,input().split()))
m = int(input())
arr_2 = list(map(int,input().split()))

for i in range(m) :
    print(binary_search(arr_1,arr_2[i],0,n-1), end=" ")


# 109236	2292