s = list(input())
word = []

for i in range(len(s)+1) :
    for j in range(i) :
        word.append("".join(s[j:i]))

word_set = set(word)

print(len(word_set))