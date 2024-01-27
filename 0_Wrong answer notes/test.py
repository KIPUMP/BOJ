# 재귀 1 3 5 7 9 - > 9 7 5 3 1

# For 문 주사위 3 개  던져서 나오는 값 전부 출력

"""
def run(n) :
    if n == 6 :
        return 
    print(n,end=" ")
    run(n+1)
    print(n,end=" ")

run(1)

"""
from itertools import combinations_with_replacement

arr = [1,2,3,4,5,6]

for i in combinations_with_replacement(arr,3) :
    print(*i)
    