# https://www.acmicpc.net/problem/1914
import sys
sys.setrecursionlimit(10**6)                # 재귀 깊이 설정

def hanoi(n,start,mid,end) :
    
    if n == 1 :                             # 돌을 하나 옮 길 때
        print(start,end,sep=" ")
        return
    
    else :
        
        hanoi(n-1,start,end,mid)        # 가장 아래 돌 빼고 중간으로 옮긴다
            
        hanoi(1,start,mid,end)          # 가장 아래 돌을 옮기고 싶은 위치로 옮긴다
            
        hanoi(n-1,mid,start,end)        # 나머지 돌들을 옮긴다.
        
        
n = int(input())
cnt = 2 ** n - 1                        # 점근적 풀이로 도출 
print(cnt)
if n <= 20 :
    hanoi(n,1,2,3)
        
    
    



