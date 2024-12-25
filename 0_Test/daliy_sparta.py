# 항해 99 [새 탭으로 깨우는 알고리즘 두뇌] 1일 1문제 풀이입니다.
# Python 코딩테스트 IDE 연습장으로 사용 가능

def quick_sort(arr) :
    if len(arr) <= 1 :
        return arr
    
    else :
        pivot = arr[0]
        arr = arr[1:]
        
        left_side = [i for i in arr if i <= pivot]
        right_side = [i for i in arr if i > pivot]
        
        return quick_sort(left_side) + pivot + quick_sort(right_side)
    
def binary_search(arr,target,start,end) :
    if start > end :
        return False
    
    else :
        mid = (start + end) // 2 
        
        if arr[mid] == target :
            return True
        
        elif arr[mid] < target :
            return binary_search(arr,target,start,mid-1)
        
        else :
            return binary_search(arr,target,mid+1,end)