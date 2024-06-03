word = input()
suffix = []

for i in range(len(word)) :
  suffix.append(word[i:])

suffix.sort()

for i in suffix :
  print(i)