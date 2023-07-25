N = int(input())
time_to_get_money = list(map(int,input().split()))
time_to_get_money.sort()

sum_val = 0
for i in range(N+1) :
  sum_val += sum(time_to_get_money[:i])

print(sum_val)
