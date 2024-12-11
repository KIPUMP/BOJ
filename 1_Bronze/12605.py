# https://www.acmicpc.net/problem/12605
import sys
input = sys.stdin.readline

n = int(input())

for i in range(1,n+1) :
    word = []
    sentence = list(input().split())
    for j in sentence :
        word.append(j)
    
    word.append(f"Case #{i}:")
    word.reverse()

    for j in word :
        print(j, end=" ")
    print()
    
# 32412	32