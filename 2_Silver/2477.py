# https://www.acmicpc.net/problem/2477
# ┏,┗,┛ 모양의 육각형 참외밭에서 자라는 참외의 수를 구하는 프로그램
# unsolved : https://itcrowd2016.tistory.com/84(해설 참고)

k = int(input())
arr = [list(map(int,input().split())) for _ in range(6)]

width = 0                       # 가장 긴 가로 길이
height = 0                      # 가장 긴 세로 길이

w_idx = 0                       # 가장 긴 가로 길이 인덱스
h_idx = 0                       # 가장 긴 세로 길이 인덱스

for i in range(6) :
    if arr[i][0] == 1 or arr[i][0] == 2 :           
        if width < arr[i][1] : 
            width = arr[i][1]
            w_idx = i
            
    elif arr[i][0] == 3 or arr[i][0] == 4 :
        if height < arr[i][1] :    
            height = arr[i][1]
            h_idx = i

s_height = abs(arr[(w_idx - 1) % 6][1] - arr[(w_idx + 1) % 6][1])   # 가장 긴 가로의 길이의 좌,우의 세로 길이를 뺀후 절댓값
s_width = abs(arr[(h_idx - 1) % 6][1] - arr[(h_idx + 1) % 6][1])    # 가장 긴 세로의 길이의 좌,우의 가로 길이를 뺀후 절댓값


area = (width * height - (s_width * s_height))
print(area * k)
