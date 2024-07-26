# https://www.acmicpc.net/problem/11478
s = list(input().strip())
word_set = set()                      # 중복을 피하기 위한 set

for i in range(1,len(s)+1) :          # 문자열 배열 슬라이싱
  for j in range(i) :
    word = "".join(s[j:i])            # 부분 문자 만들기
    word_set.add(word)

print(len(word_set))

#240872	2036