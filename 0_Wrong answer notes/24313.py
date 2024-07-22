#https://www.acmicpc.net/problem/24313
# 해법 : 수식화 + 양수 조건 추가

a1,a0 = map(int,input().split())            
c = int(input())
n0 = int(input())

if a0 <= (c-a1)*n0 and a1 <= c:             # 양의 정수 조건을 추가해주어야 다음 식의 점근적 표기 기법 성립
    print(1) 
else :
    print(0)
    
# 31120	44