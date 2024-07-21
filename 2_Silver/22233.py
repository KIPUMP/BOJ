import sys
input = sys.stdin.readline

keyword_dict = {}
n,m = map(int,input().split())

for _ in range(n) :
    keyword = input().strip()
    keyword_dict[keyword] = 1
    
for _ in range(m) :
    memo = input().strip().split(',')       # strip()을 사용하면 입력받을 때 '\n'이 사라짐
    for i in memo :
        if i in keyword_dict :
            del keyword_dict[i]
    print(len(keyword_dict))
            

