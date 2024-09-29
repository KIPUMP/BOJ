# https://www.acmicpc.net/problem/31848

n = int(input())
hole = list(map(int, input().split()))
q = int(input())
acorn = list(map(int, input().split()))

result = []

# 구멍을 순차적으로 탐색하며 도토리가 통과 가능한지 확인
for acorn_size in acorn:
    current_size = acorn_size
    position = -1  # 도토리가 들어갈 수 있는 구멍이 없으면 -1로 유지
    
    for i in range(n):
        if current_size <= hole[i]:  # 도토리가 구멍을 통과할 수 있는 경우
            position = i + 1  # 구멍의 위치는 1부터 시작
            break
        current_size -= 1  # 구멍을 통과할 때마다 도토리 크기 감소
    
    result.append(position)

# 결과 출력
print(*result)
