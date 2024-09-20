# 두 수 사이의 피보나치 수들의 합을 구하는 함수
def fibonacci_sum_in_range(low, high):
    # 피보나치 초기값
    a, b = 1, 2
    result = 0
    
    # 피보나치 수열을 생성하며 조건에 맞는 값들을 찾는다
    while a <= high:
        if low <= a <= high:
            result += a
        # 피보나치 수 갱신
        a, b = b, a + b
    
    return result

# 주어진 범위
low = 12345678999
high = 99987654321

# 피보나치 수의 합을 계산
result = fibonacci_sum_in_range(low, high)
print(result)