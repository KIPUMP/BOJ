from collections import deque
import sys
input = sys.stdin.readline

n = list(input().strip())  

left = deque(n)
right = deque()

for _ in range(int(input())):
    command = list(input().split())                 # 명령

    if command[0] == 'L' :
        if left :
            right.appendleft(left.pop())           #왼쪽 리스트 끝의 원소 오른쪽에 삽입   

    elif command[0] == 'D' :
        if right :
            left.append(right.popleft())           #오른쪽 리스트 완쪽 끝의 원소를 왼쪽리스트에 삽입 
        
    elif command[0] == 'B' :
        if left :
            left.pop()                            # left에 원소 있다면 제거

    elif command[0] == "P" :
        left.append(command[1])

result = left + right

print(*result,sep="")


