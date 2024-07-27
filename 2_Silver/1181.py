# https://www.acmicpc.net/problem/1181
import sys
input = sys.stdin.readline

n = int(input())
word = []

for _ in range(n) :
  word.append(input())

word = sorted(set(word)) # 중복 제거 
word = sorted(word, key = lambda x : len(x)) # 길이 정렬

for i in word :
  print(i,end="")


# 35732	84