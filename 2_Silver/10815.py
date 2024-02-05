n = int(input())
own_card = sorted(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))


def binary_search(arr, target, start, end):
    if start > end:
        return False
    else:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            return binary_search(arr, target, mid + 1, end)
        else:
            return binary_search(arr, target, start, mid - 1)


result = [0] * m

for i in range(m):
    result[i] = 1 if binary_search(own_card, arr[i], 0, n - 1) else 0

print(*result)
