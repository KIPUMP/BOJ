# https://www.acmicpc.net/problem/25178

# 시작과 끝이 같은 지 판별하는 함수
def is_equal_start_end(s1,s2) :
    if s1[0] == s2[0] and s1[-1] == s2[-1]:
        return True
    return False
    
# 모음 판별 하고 제거하는 함수
def remove_vowels(s) :
    vowels = ['a','e','i','o','u']
    for i in vowels :
        s = s.replace(i,'')
    return s.strip()

# 문자열 원소가 같은지 판별하는 함수        
def is_same(s1,s2) :
    return sorted(s1) == sorted(s2)
    
n = int(input())
word_1 = input()
word_2 = input()

if is_equal_start_end(word_1,word_2) :
    word_shortten_1 = remove_vowels(word_1)
    word_shortten_2 = remove_vowels(word_2)
    if word_shortten_1 == word_shortten_2 :
        if is_same(word_1,word_2) :
            print("YES")
        else :
            print("NO")
    else :
        print("NO")
else :
    print("NO")

# 33044	68