# while 문 시간 초과 
# 점화식 추론
hurt_finger = int(input())
count = int(input())
result = 0
if hurt_finger == 1 :
    if count == 0 :
        result = 0
    else :
        result = count * 8
        
elif hurt_finger == 5 :
    if count == 0 :
        result = 4
    else :
        result = 4 + count * 8    
        
else :
    if count == 0 :
        result = hurt_finger - 1
    else :
        result = 4 * count + 1
        
        if count % 2 == 0 :
            result += hurt_finger -2
            
        else :
            result += 4 - hurt_finger
    
print(result)        

        
        