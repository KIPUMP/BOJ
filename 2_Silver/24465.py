month = [1,2,3,4,5,6,7,8,9,10,11,12]
day = [20,19,21,20,21,22,23,23,23,23,23,22]
star = ['물병','물고기','양','황소','쌍둥이','게','사자','처녀','천칭','전갈','사수','염소']
member_birth = []

for _ in range(7) :
    member_month, member_day = map(int,input().split())
    for i in range(12) :
        if month[i] == member_month :
            if day[i] <= member_day :
                member_birth.append(star[i])
            else :
                member_birth.append(star[i-1])


n = int(input()) 
result = []

for _ in range(n) :
    x, y = map(int,input().split())
    people = ''
    for i in range(12) :
        if month[i] == x :
            if day[i] <= y :
                people = star[i]
            else :
                people = star[i-1]
                
    if people not in member_birth :
        result.append((x,y))

result.sort()

if len(result) == 0 :
    print('ALL FAILED')
else :
    for i in result :
        print(*i)
    
        
    
    