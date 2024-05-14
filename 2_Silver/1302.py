import sys
input = sys.stdin.readline

n = int(input())
book_store = {}

for _ in range(n) :
  book_name = input()

  if book_name in book_store :
    book_store[book_name] += 1
  else :
    book_store[book_name] = 0
  

max_val = max(book_store.values())

result = []
for i in book_store.keys() :
  if book_store[i] == max_val :
    result.append(i)

result.sort()
print(result[0])


