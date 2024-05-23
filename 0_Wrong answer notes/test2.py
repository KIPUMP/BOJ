t = int(input())

for i in range(t) :
    n = int(input())
    arr_1 = list(map(int,input().split()))
    arr_2 = list(map(int,input().split()))
    result = 0
    for j in arr_1 :
        for k in arr_2 :
            if (j-3) < 0 :
                if 1 <= k <= (j+3) :
                    result += 1
                    break
                
            elif (j+3) > 2000 :
                if (j-3) <= k <= 2000 :
                    result += 1
                    break

            else :
                if (j-3) <= k <= (j+3) :
                    result += 1
                    break

    print(f"#{i+1} {result}")
                