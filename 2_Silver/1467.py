e,s,m = map(int,input().split())

year_earth,year_sun,year_moon = 0,0,0
result = 0

while True :
    
    if year_earth == e and year_sun == s and year_moon == m :
        print(result)
        break
    
    year_earth += 1
    year_moon += 1
    year_sun += 1
    result += 1
    
    if year_earth > 15 :
        year_earth = 1
    
    if year_sun > 28 :
        year_sun = 1
        
    if year_moon > 19 :
        year_moon = 1
        
        

    
    
