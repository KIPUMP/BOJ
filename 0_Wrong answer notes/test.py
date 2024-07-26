# def selection_sort(arr) :
#     for i in range(len(arr)) :
#         min_idx = i
#         for j in range(i+1, len(arr)) :
#             if arr[j] < arr[min_idx] :
#                 min_idx = j                         # 가장 작은 원소의 인덱스 기록
            
#         arr[i],arr[min_idx] = arr[min_idx], arr[i]  # 교환

#     return arr

# def insertion_sort(arr) :
#     for i in range(1,len(arr)) :                # 첫번째 원소는 정렬되어 있다고 가정
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key < arr[j] :         # 인덱스가 0이 될때까지 + key > arr[j] 멈춤
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = key
#     return arr

# def quick_sort(arr) :
#     if len(arr) <= 1 :
#         return arr
#     else :
#         pivot = arr[0]
#         arr = arr[1:]
#         left = [i for i in arr if i <= pivot]
#         right = [i for i in arr if i > pivot]

#         return quick_sort(left) + [pivot] + quick_sort(right)

def counting_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    result = []
    for i, c in enumerate(count):
        print(i,c)
        result.extend([i] * c)
    return result

arr = list(map(int,input().split()))       

# print(selection_sort(arr))
# print(insertion_sort(arr))
# print(quick_sort(arr))
print(counting_sort(arr))
