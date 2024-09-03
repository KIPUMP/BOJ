import sys
input = sys.stdin.readline

while True : 
    triangle = sorted(map(int,input().split()))
    
    triangle_set = list(set(triangle))
    
    if len(triangle_set) == 1 :
        if triangle[0] == 0 :
            break
        
        else :
            print("Equilateral")
            
    elif len(triangle_set) == 2 :
        if triangle[0] + triangle[1] <= triangle[2] :
            print("Invalid")
            
        else :
            print("Isosceles")
        
    
    else :
        if triangle[0] + triangle[1] <= triangle[2] :
            print("Invalid")
        else :
            print("Scalene")
            
# 	31120	32