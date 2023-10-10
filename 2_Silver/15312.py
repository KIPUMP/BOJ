convert = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
a = input()
b = input()
result = []

for i in range(len(a)) :
    
    result.append(convert[ord(a[i]) - 65])
    result.append(convert[ord(b[i]) - 65])


temp = []

while len(result) > 2 :
    for i in range(1,len(result)) :
        temp.append((result[i] + result[i-1]) % 10)

    result = temp
    temp = []
print(f"{result[0]}{result[1]}")