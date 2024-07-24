from collections import deque

n,k = map(int,input().split())
students = [i for i in range(1,n+1)]
queue = deque(students)

result = []
while queue :                   
    for _ in range(k-1) :                   # 가장 첫 값을 k번째로 바꿈
        queue.append(queue.popleft())
    
    result.append(queue.popleft())          # k 번째 결과 값 넣기 
    
print(str(result).replace('[','<').replace(']','>'))
    