import heapq
import sys

N = int(input())
card_deck = []
for _ in range(N) :
  heapq.heappush(card_deck, int(sys.stdin.readline()))

if len(card_deck) == 1 :
  print(0)
else :
  cnt = 0
  while len(card_deck) > 1 :
    min_val_1 = heapq.heappop(card_deck)
    min_val_2 = heapq.heappop(card_deck)
    cnt += min_val_1 + min_val_2
    heapq.heappush(card_deck,min_val_1+min_val_2)
  print(cnt)