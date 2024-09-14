# https://www.acmicpc.net/problem/8979
import sys
input = sys.stdin.readline

# 입력 처리
n, k = map(int, input().split())
countries = []

for _ in range(n):
    country_info = list(map(int, input().split()))
    country = country_info[0]
    gold = country_info[1]
    silver = country_info[2]
    bronze = country_info[3]
    countries.append((country, gold, silver, bronze))

# 메달 수를 기준으로 정렬 (금 -> 은 -> 동 순으로 내림차순)
countries.sort(key=lambda x: (-x[1], -x[2], -x[3]))

# 국가의 순위 계산
rank = 1
rank_dict = {}
rank_dict[countries[0][0]] = rank

for i in range(1, n):
    if countries[i][1:] == countries[i - 1][1:]:
        # 메달 수가 같으면 이전 국가와 동일한 순위
        rank_dict[countries[i][0]] = rank
    else:
        # 메달 수가 다르면 현재 국가의 순위는 i + 1
        rank = i + 1
        rank_dict[countries[i][0]] = rank

# 주어진 국가 k의 순위 출력
print(rank_dict[k])


# 	31120	32