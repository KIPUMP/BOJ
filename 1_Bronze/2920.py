song = map(int,input().split())
ASE_cnt = 0
DESC_cnt = 0
for i in range(1,9) :
  if song[i-1] == i :
    ASE_cnt += 1

for i in range(7,-1,-1) :
  if song[i] == i+1 :
    DESC_cnt += 1


if ASE_cnt == 8:
  print("ascending")
elif DESC_cnt == 8 :
  print("descending")
else :
  print("mixed")




      