# https://www.acmicpc.net/problem/1924
# 2007년의 특정 년 월의 요일을 구하는 문제

days = [31,28,31,30,31,30,31,31,30,31,30,31]        # 달별 일 수
today = ['SUN','MON','TUE','WED','THU','FRI','SAT'] # 요일 

x,y = map(int,input().split())                      # 목표 날짜
t_month, t_day = 1,1                                # default 날짜
d_idx = 1                                           # 요일 인덱스

while True :
    
    if t_month == x and t_day == y :                # 목표한 날짜가 된다면
        print(today[d_idx % 7])                     # 요일 출력 후 반복 탈출
        break
    
    t_day += 1                                      # 다음날
    d_idx += 1                            
    
    if days[t_month - 1] < t_day :                  # 달이 변한다면 일을 1로 초기화
        t_day = 1
        t_month += 1
    
    
    
    

