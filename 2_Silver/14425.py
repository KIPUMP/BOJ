import sys
input_func = sys.stdin.readline

word_list = {}
cnt = 0

n, m = map(int, input_func().split())

for _ in range(n):
    word = input_func().strip()
    word_list[word] = True

for _ in range(m):
    word = input_func().strip()
    if word in word_list:
        if word_list[word] == True:
            cnt += 1

print(cnt)
