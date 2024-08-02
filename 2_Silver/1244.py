import sys
input = sys.stdin.readline

def switch_light(n) :
    if n == 1 :
        return 0
    else :
        return 1

n = int(input())                                # 스위치 개수
switch = list(map(int,input().split()))         # 스위치
students = int(input())                         # 학생 수
for _ in range(students) :
    gender, number = map(int,input().split())       # 성별 , 숫자
    # 남학생
    if gender == 1 :
        for i in range(number-1,n,number) :
            switch[i] = switch_light(switch[i])
        # print(*switch)
    # 여학생
    else :
        min_size = min(len(switch[:number-1]),len(switch[number:]))
        switch[number-1] = switch_light(switch[number-1])
        # print(*switch)
        for i in range(1,min_size+1) :
            if switch[number-i-1] != switch[number+(i-1)] :
                break
            else :
                switch[number-i-1] = switch_light(switch[number-i-1])
                switch[number+(i-1)] = switch_light(switch[number+(i-1)])

for i in range(0,n,20) :
    print(*switch[i:i+20])
    
# 31120	40