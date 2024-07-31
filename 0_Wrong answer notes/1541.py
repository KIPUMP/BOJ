# https://www.acmicpc.net/problem/1541
# 숫자와 숫자 사이에는 괄호 x ( 55 - (50+40) = -35)
# +의 숫자를 모두 더해준후 

# 입력 수식 읽기
expression = input().strip()

# '-'로 수식 분할하기
parts = expression.split('-')
print(parts)

# 첫 번째 부분의 합 계산하기
initial_sum = 0

# 나머지 부분의 합 계산하기
remaining_sum = 0


for part in parts[1:]:
    # 각 부분에서는 '-'가 없으므로 '+'로 나누어 숫자 합산하기
    part_sum = sum(map(int, part.split('+')))
    remaining_sum += part_sum

# 결과 계산: 첫 번째 부분의 합에서 나머지 부분의 합을 빼기
result = initial_sum - remaining_sum

print(result)
