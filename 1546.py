n = int(input())
grade = list(map(int,input().split()))
max_val = max(grade)
sum_val = 0
for i in grade  :
    sum_val += (i/max_val)*100


avg = sum_val / n
print(avg)