# 항해 99 [새 탭으로 깨우는 알고리즘 두뇌] 1일 1문제 풀이입니다.
# Python 코딩테스트 IDE 연습장으로 사용 가능

n = int(input())

work_list = [list(input().split()) for _ in range(n)]

work_list = sorted(work_list, key = lambda x : (int(x[1]),int(x[2]),x[0]))

print(work_list)