a,p = map(int,input().split())

visited = {}
current = a
idx = 1

while current not in visited.keys() :
    visited[current] = idx
    num = 0
    for i in str(current) :
        num += int(i) ** p
        
    current = num
    idx += 1
    
first_repeat_idx = visited[current] - 1
remaining_sequence = list(visited.values())[ : first_repeat_idx]

print(len(remaining_sequence))
    