string_arr = list(input().rstrip())

result = []

for i in range(len(string_arr)):
    for j in range(i+1, len(string_arr)+1):
        result.append("".join(string_arr[i:j]))

a = set(result)

print(len(a))