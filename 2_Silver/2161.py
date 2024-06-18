from collections import deque
n = int(input())

card = deque()

for i in range(1,n+1) :
    card.append(i)

abandon_card = []

while True :
    if len(card) == 1:
        break
    
    x = card.popleft()
    y = card.popleft()
    
    abandon_card.append(x)
    card.append(y)
    
for i in abandon_card :
    print(i,end=" ")

for i in card :
    print(i,end=" ")    
    
    

