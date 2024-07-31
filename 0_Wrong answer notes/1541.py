# https://www.acmicpc.net/problem/1541
# 숫자와 숫자 사이에는 괄호 x ( 55 - (50+40) = -35)
# +의 숫자를 모두 더해준후 

arr = input().split('-')
s= 0
for i in arr[0].split('+') :
  s += int(i)
for i in arr[1:] :
  for j in i.split('+') :
    s-=int(j)
print(s)

#31256	40