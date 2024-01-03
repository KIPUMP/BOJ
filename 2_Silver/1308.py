odd_year = [1,3,5,7,8,10,12]
even_year = [4,6,9,11]

today = list(map(int,input().split()))
d_day = list(map(int,input().split()))
cnt = 0

while True:
    
    if today == d_day :
        print(f"D-{cnt}")
        break
    
    if d_day[0] > today[0] + 1000:
        print("gg")
        break
    
    if today[0] + 1000 == d_day[0] and (today[1], today[2]) <= (d_day[1],d_day[2]) :
        print("gg")
        break

    
    today[2] += 1
    cnt += 1

    if today[1] in odd_year :
        if today[2] > 31 :
            today[1] += 1
            today[2] = 1
            if today[1] > 12 :
                today[0] += 1
                today[1] = 1
                
    elif today[1] in even_year :
        if today[2] > 30 :
            today[1] += 1
            today[2] = 1

                
    else :
        if today[0] % 4 == 0 :
            if today[0] % 100 == 0 :
                if today[0] % 400 == 0 :
                    if today[2] > 29 :
                        today[1] += 1
                        today[2] = 1
                        
                else :
                    if today[2] > 28 :
                        today[1] += 1
                        today[2] = 1
            else :
                if today[2] > 29 :
                    today[1] += 1
                    today[2] = 1
        else :
            if today[2] > 28 :
                today[1] += 1
                today[2] = 1
        
        
        
        