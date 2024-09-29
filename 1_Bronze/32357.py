# https://www.acmicpc.net/problem/32357
import sys
input = sys.stdin.readline

arr = []
count = 0
n = int(input())

for _ in range(n) :
    word = list(input().rstrip())
    reversed_word = word[::-1]

    if word == reversed_word :
        count += 1

if count <= 1 :
    print(0)
    
else :
    print(count*(count-1))


# 31120	160