# https://www.acmicpc.net/problem/1157
word = list(input().rstrip().lower())
word_set = set(word)
word_dict = {}

for i in word_set :
    word_dict[i] = word.count(i)
    
    
max_val = max(word_dict.values())
cnt = 0
key = ''
for i in word_dict.keys() :
    if max_val <= word_dict[i] :
        key = i
        cnt += 1
        

if cnt > 1 :
    print('?')
else :
    print(key.upper())