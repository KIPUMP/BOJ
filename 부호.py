while True:
    n = int(input())
    sum = 0
    for i in range(0,n) :
        x = int(input())
        sum += x

    if sum > 0 :
        print("+")
    elif sum < 0 :
        print("-")
    else :
        print("0")