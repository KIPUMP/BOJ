n,m = map(int,input().split())
trees = list(map(int,input().split()))
start, end = 0, max(trees)
mid = (start + end) // 2

def get_total(h) :
    result = 0
    for t in trees :
        if t >= h :
            result += t - h
        
    return result

result = 0
while start <= end :
    if get_total(mid) >= m :
        result = mid
        start = mid + 1
        
    else :
        end = mid - 1
    mid = (start + end) // 2

print(result)

