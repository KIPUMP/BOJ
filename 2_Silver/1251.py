word = list(input().rstrip())
result = []
for i in range(1,len(word)-1) :
    for j in range(i+1,len(word)) :
        first_word = word[:i]
        second_word = word[i:j]
        third_word = word[j:]
        
        first_word.reverse()
        second_word.reverse()
        third_word.reverse()
        
        result.append("".join(first_word+second_word+third_word))
        
        
        
print(min(result))
