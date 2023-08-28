from itertools import permutations

N, M = map(int, input().split())
items = [i for i in range(1,N+1)]
for i in permutations(items, M):
    print(*i)
