n = int(input())
word = input()
hash_result = 0

for i in range(n) :
  hash_result += (ord(word[i])-96) * (31 ** i)

print(hash_result % 1234567891)