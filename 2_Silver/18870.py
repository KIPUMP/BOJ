# 배열을 정렬 후 자신보다 작은 원소의 개수를 기록한다
# https://www.acmicpc.net/problem/18870

n = int(input())
arr = list(map(int,input().split()))
arr_sorted = sorted(set(arr))

result = dict()

for i in range(len(arr_sorted)) :
  result[arr_sorted[i]] = i


for i in range(len(arr)) :
  print(result[arr[i]], end=" ")



#	144340	1748