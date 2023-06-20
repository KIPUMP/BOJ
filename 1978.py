n = int(input())
arr = list(map(int, input().split()))
cnt = 0

for i in range(n):
    is_prime = True
    if arr[i] > 1:
        for j in range(2, int(arr[i] ** 0.5) + 1):
            if arr[i] % j == 0:
                is_prime = False
                break
    else:
        is_prime = False
    if is_prime:
        cnt += 1

print(cnt)



