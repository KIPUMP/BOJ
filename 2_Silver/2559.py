n,k = map(int,input().split())
temperature = list(map(int,input().split()))
result = []
result.append(sum(temperature[:k]))

for i in range(n-k):
    result.append(result[i] - temperature[i] + temperature[k+i])
    
print(max(result))