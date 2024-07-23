# https://www.acmicpc.net/problem/25192
# 해법 : 딕셔너리
import sys
input = sys.stdin.read
from collections import defaultdict

data = input().split()
n = int(data[0])
gom_chat = defaultdict(int)
hello_cnt = 0

for word in data[1:]:
    if word == 'ENTER':
        gom_chat = defaultdict(int)  # ENTER 할때마다 딕셔너리 초기화
    else:
        if gom_chat[word] == 0:
            hello_cnt += 1
            gom_chat[word] += 1

print(hello_cnt)


#43376	112