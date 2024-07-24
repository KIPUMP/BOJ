import sys
input = sys.stdin.readline

n = list(input().strip())                       # 문자열
m = int(input())
idx = len(n)                                    # 커서 인덱스

for i in range(int(m)) :
    command = list(input().split())             # 명령 
    
    left = n[:idx]
    right = n[idx:]
    
    if command[0] == 'L' :                      # 커서 왼쪽 이동
        if idx == 0 :
            continue
        idx -= 1

    elif command[0] == 'D' :                    # 커서 오른쪽 이동
        if idx == len(n):
            continue
        idx += 1
        
    elif command[0] == 'B' :                    # 커서 왼쪽의 문자 제거
        if idx == 0 :
            continue
        left.pop()
        idx -= 1
            
    elif command[0] == 'P' :                     # 커서 왼쪽에 문자 추가
        left.append(command[1])
        idx += 1
        
    n = left+right

print(*n,sep="")