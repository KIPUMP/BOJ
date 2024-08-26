# https://www.acmicpc.net/problem/1806

# n개의 수로 이루어진 리스트에서 연속된 수들의 부분합이 S 이상이 되는 
# 것 중, 가장 짧은 길이를 구하라

n,s = map(int,input().split())
arr = list(map(int,input().split()))

sum_a = []                      # arr 누적합 리스트
t = 0

for i in range(n) :
    t += arr[i]
    sum_a.append(t)

print(sum_a)
min_length = 0
start = 0
end = 0

for i in range(n) :
    if sum_a[i] >= s :
        end = i
        min_length = i+1
        break

while start <= end and end < n :
    if sum_a[end] - sum_a[start] < s :
        end += 1
    
    else :
        if min_length > (end - start) + 1 :
            min_length = (end-start) + 1
            start += 1
            
        else :
            end += 1
            
print(min_length)
