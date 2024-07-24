n = int(input())
cnt = 0

for _ in range(n) :
    arr=[]    
    vps = list(input().strip())             # 괄호 입력
    while True :                    
        if len(vps) == 0 :                  # vps가 0일때
            
            if len(arr) == 0 :              # arr이 0이면
                print("YES")
                break
            
            else :                          
                print("NO")
                break
            
        x = vps.pop()
        
        if x == ")" :
            arr.append(x)
            
        else :
            if len(arr) == 0 :      # arr이 0 이면 닫아줄 괄호가 없다
                print("NO")
                break
            
            else : 
                arr.pop()
