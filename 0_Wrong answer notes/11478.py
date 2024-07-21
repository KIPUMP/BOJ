# https://www.acmicpc.net/problem/11478
s = list(input())
word = []
word = set(word)

for i in range(len(s)+1) :
    for j in range(i) :
        word.add("".join(s[j:i]))

print(len(word))