# while문 시간 초과 
# 해설 : 점화식 추론
w,h = map(int,input().split())
p,q = map(int,input().split())
t = int(input())

a = (p + t) // w                # x축 증가 하는 부분인지 감소하는 부분인지 확인
b = (q + t) // h                # y축 증가 하는 부분인지 감소하는 부분인지 확인

if a % 2 == 0 :                 # x축 증가하는 부분이라면       
    x = (p + t) % w
else :                          # x축 감소하는 부분이라면
    x = w - (p + t) % w
    
if b % 2 == 0 :                 # y축 증가하는 부분이라면
    y = (q + t) % h
else :                          # y축 감소하는 부분이라면
    y = h - (q + t) % h
    
print(x,y)
    
