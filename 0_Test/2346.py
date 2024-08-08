from collections import deque

n = int(input())
arr = list(map(int,input().split()))  # 풍선에 적힌 숫자 리스트
queue = deque(enumerate(arr))

while True:
    idx,x = queue.popleft()  # 현재 풍선을 터뜨림
    print(idx + 1, end=" ")  # 원래 인덱스 출력 (1-based index)

    if not queue:  # 큐가 비어있으면 종료
        break

    if x < 0:  # 숫자가 음수일 경우 왼쪽으로 이동
        for i in range(x * -1):
            queue.appendleft(queue.pop())
    else:  # 숫자가 양수일 경우 오른쪽으로 이동
        for i in range(x - 1):
            queue.append(queue.popleft())

#34028	104