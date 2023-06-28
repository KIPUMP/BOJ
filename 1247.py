import sys
result = []
for _ in range(3) :
    arr =  []
    n = int(sys.stdin.readline())

    for _ in range(n) :
        arr.append(int(sys.stdin.readline()))

    if sum(arr) > 0 :
        result.append("+")
    elif sum(arr) < 0 :
        result.append("-")
    else :
        result.append("0")


for i in result :
    print(i)