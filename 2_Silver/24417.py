n = int(input())
d = [0] * (n+1)

d[1] = 1
d[2] = 1

def solution(n) :
    if n <= 2 :
        return d[n]
    else :
        for i in range(3,n+1) :
            d[i] = d[i-1] + d[i-2]
            
        return d[n]


recursive_cnt = solution(n) % 1000000007
dynamic_programming_cnt = (n-2) % 1000000007

print(recursive_cnt, dynamic_programming_cnt)
