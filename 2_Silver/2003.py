# https://www.acmicpc.net/problem/2003
# 해결  : 투 포인터(알고리즘 분류 참고)
# 투 포인터
# 메모리 : 32140 , 시간 : 484

n,m = map(int,input().split())
arr = list(map(int,input().split()))
left, right = 0,0             # 왼쪽 인덱스 , 오른쪽 인덱스 
cnt = 0         

while right <= n and left <= right :          # 반복 조건 부여
    total = sum(arr[left:right])              # 합 구하기
    
    if total == m :                           # m과 같다면 오른쪽 인덱스 1 추가
      cnt += 1
      right += 1                                
    elif total < m :                          # 작다면 → 오른쪽 인덱스를 1 증가시켜서 합을 증가시킨다
      right += 1            
    else :                                    # 크다면 → 왼쪽 인덱스를 1 증가시켜서 합을 감소시킨다.
      left += 1
      
print(cnt)
