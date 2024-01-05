from collections import deque
n = int(input())
card = deque()
card.append(n)

for i in range(n-1,0,-1) :
    card.appendleft(i)
    for _ in range(i) :
        card.appendleft(card.pop())
        
print(*card)