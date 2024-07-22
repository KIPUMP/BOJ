# https://www.acmicpc.net/problem/25192
# 해법 : 딕셔너리
from collections import defaultdict

n = int(input())
gom_chat = defaultdict(int)
hello_cnt = 0

for _ in range(n) :
    word = input()
    if word == 'ENTER' :
        gom_chat = defaultdict(int)     # ENTER 할때마다 딕셔너리 초기화
    
    else :
        if gom_chat[word] == 0  :       
            hello_cnt += 1
            gom_chat[word] += 1

print(hello_cnt)


#39560	4008