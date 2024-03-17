n,jimin_number,hansu_number = map(int,input().split())

cnt = 0 
while jimin_number != hansu_number :

  jimin_number -= jimin_number // 2
  hansu_number -= hansu_number // 2
  cnt += 1

print(cnt)