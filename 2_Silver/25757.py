# https://www.acmicpc.net/problem/25757

n,game = input().split()

people = []
for i in range(int(n)) :
    people.append(input())
    
people = list(set(people))              # 중복 X 인원

if game == 'Y' :                        # 1명 필요한 게임
    print(len(people))

elif game == 'F' :                      # 2명 필요한 게임
    count = 0
    playing_people = 0                  # 명 수가 충족되는 지 판단
    for _ in range(len(people)) :
        playing_people += 1
        if playing_people == 2 :
            count += 1
            playing_people = 0
    print(count)

else :                                  # 3명 필요한 게임
    count = 0
    playing_people = 0
    for _ in range(len(people)) :
        playing_people += 1
        if playing_people == 3 :
            count += 1
            playing_people = 0
    print(count)
        
# 44196	2392