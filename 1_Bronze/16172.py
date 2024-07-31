# https://www.acmicpc.net/problem/16172

def remove_digit(s) :
    return ''.join(filter(lambda x : not x.isdigit(),s))

def compute_LPS_arr(pattern) :
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    while i < m :
        if pattern[i] == pattern[length] :
            length += 1
            lps[i] += length
            i += 1
        else :
            if length != 0 :
                length = lps[length - 1]
            else :
                lps[i] = 0
                i += 1
    return lps

def KMP_search(text,pattern) :
    n = len(text)
    m = len(pattern)
    lps = compute_LPS_arr(pattern)
    
    i = 0
    j = 0
    
    while i < n :
        if pattern[j] == text[i] :
            i += 1
            j += 1
        if j == m :
            return True
        elif i < n and pattern[j] != text[i] :
            if j != 0 :
                j = lps[j-1]
            else :
                i += 1
                
    return False

s = input().strip()
k = input().strip()

s_without_digit = remove_digit(s)
if KMP_search(s_without_digit,k) :
    print(1)
else :
    print(0)

# 35436	140