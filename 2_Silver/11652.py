import sys
input = sys.stdin.readline

n = int(input())

card_deque = {}

for _ in range(n) :
    card = int(input())
    
    if card in card_deque :     # 딕서너리에서 키 값을 기준으로 찾는다
        card_deque[card] += 1
        
    else :
        card_deque[card] = 1
        
result = []
max_val = max(card_deque.values())

for i in card_deque.keys() :
    if card_deque[i] == max_val :
        result.append(i)
        

result.sort()

print(result[0])