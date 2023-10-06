def solution(phone_book):
    phone_list = sorted(phone_book)
    for a, b in zip(phone_list, phone_list[1:]):
      if b.startswith(a):
          return False
    return True
phone_book = ["123","456","789"]
solution(phone_book)
