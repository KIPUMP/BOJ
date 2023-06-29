arr_left = []
for _ in range(10) :
  n = int(input())
  arr_left.append(n%42)

arr = set(arr_left)
print(len(arr))