# https://www.acmicpc.net/problem/4659
import sys
input = sys.stdin.readline

vowels = ['a','e','i','o','u']

def is_acceptable(word) :
    has_vowel = False
    vowel_combo = 0
    consonant_combo = 0
    
    for i in range(len(word)) :
        if word[i] in vowels :
            has_vowel = True
            vowel_combo += 1
            consonant_combo = 0
        else :
            consonant_combo += 1
            vowel_combo = 0
            
        if vowel_combo == 3 or consonant_combo == 3 :
            return False
        
        if i > 0 and word[i] == word[i-1] :
            if word[i] not in ['e','o'] :
                return False

    return has_vowel


while True :
    word = input().rstrip()
    
    if word == 'end' :
        break
    
    if is_acceptable(word) :
        print(f"<{word}> is acceptable.")
        
    else :
        print(f"<{word}> is not acceptable.")
        
        
# 31120	32