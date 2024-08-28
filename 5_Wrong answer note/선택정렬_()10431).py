# https://www.acmicpc.net/problem/10431
# 선택 정렬의 횟수 count

def selection_sort(arr) :
    global count
    for i in range(len(arr)) :
        for j in range(len(arr)-1) :
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count += 1


p = int(input())
for t in range(1,p+1) :
    arr = list(map(int,input().split()))        # 순서, 리스트
    arr = arr[1:]         
    count = 0          
    selection_sort(arr)
    print(t,count)
    
    
# 31120	116