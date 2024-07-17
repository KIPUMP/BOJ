# https://www.acmicpc.net/problem/2480
# 3개의 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램 작성

dice = list(map(int,input().split()))       # 주사위 3개 눈 입력

if dice[0] == dice[1] :                     # 1 번째 주사위와 2 번쨰 주사위가 같다면                    
    if dice[0] == dice[2] :                 # 2 번째 주사위와 3 번쨰 주사위가 같다면(모두 같다면)
        print(10000 + (dice[0] * 1000))
    else :                                                               
        print(1000 + (dice[1] * 100))

elif dice[0] == dice[2] :                   # 1 번째와 3번째가 같음
    if dice[0] == dice[1] :                 # 3개의 눈이 모두 같음
        print(10000 + (dice[0] * 1000))
    else :
        print(1000 + (dice[0]*100))

else :
    if dice[1] == dice[2] :                 # 2 번째와 3번째가 같음
        print(1000 + (dice[1] * 100))
    else :
        print(max(dice) * 100)

