# https://www.acmicpc.net/problem/9663
import sys

input = sys.stdin.readline

N = int(input())  # N값 입력받기

arr = [0] * N  # 각 행에 퀸이 위치한 열 정보를 저장

def is_possible(r):
    # r번째 행에 배치된 퀸이 이전 퀸들과 충돌하지 않는지 확인
    for i in range(r):
        if arr[r] == arr[i] or abs(arr[r] - arr[i]) == abs(r - i):
            return False
    return True

def dfs(row):
    global answer
    # 모든 퀸을 배치한 경우
    if row == N:
        answer += 1
        return 

    for col in range(N):
        arr[row] = col
        if is_possible(row):
            dfs(row + 1)

answer = 0
# 결과 출력
dfs(0)

print(answer)


# 참고 : https://seongonion.tistory.com/103
# 198268	28328