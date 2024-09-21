# https://www.acmicpc.net/problem/9017
import sys
from collections import Counter , defaultdict
input = sys.stdin.readline

for _ in range(int(input())) :                      # 테스트 케이스
    n = int(input())                                # 기록의 수
    ranking = list(map(int,input().split()))        # 결과 기록
    
    team_set = set(ranking)                         # 팀 목록
    
    team_count = Counter(ranking)

  
    # 6명 미만인 팀은 제외
    ranking = [x for x in ranking if team_count[x] >= 6]

    # 각 팀의 선수 순위를 저장할 딕셔너리
    team_dict = defaultdict(list)
    
    for i in range(len(ranking)):
        team_dict[ranking[i]].append(i + 1)  # 순위는 1-based (1부터 시작)
    
    total = []
    min_rank_5th = {}

    # 각 팀의 상위 4명의 순위 합산과 5등 선수 순위 저장
    for team, ranks in team_dict.items():
        # 상위 4명 순위 합산
        sum_val = sum(ranks[:4])
        total.append((sum_val, team))
        
        # 5등 선수의 순위를 저장 (동점일 시 사용)
        if len(ranks) >= 5:
            min_rank_5th[team] = ranks[4]
        else:
            min_rank_5th[team] = float('inf')  # 5등 선수가 없으면 아주 큰 값으로 처리
    
    # 상위 4명의 순위 합으로 정렬, 동점일 경우 5등 선수 순위로 정렬
    total.sort(key=lambda x: (x[0], min_rank_5th[x[1]]))

    # 결과 출력 (순위 합이 가장 작은 팀)
    print(total[0][1])
    
# 34072	64