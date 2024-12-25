# https://www.acmicpc.net/problem/2467

n = int(input())
arr = list(map(int, input().split()))

start = 0
end = n - 1

min_sum = int(1e9) * 2
result = []

while start < end:
    current_sum = arr[start] + arr[end]
    
    if abs(current_sum) < abs(min_sum):
        min_sum = current_sum
        result = [arr[start], arr[end]]
    
    if current_sum < 0:
        start += 1
    else:
        end -= 1

print(*result)


# 44748	116