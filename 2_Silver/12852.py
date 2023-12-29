n = int(input())
mem = [0] * (n+1)
path = ["" for _ in range(n+1)]
path[1] = "1"

for i in range(2,n+1) :
    mem[i] = mem[i-1] + 1
    prev = i - 1
    
    if i % 3 == 0 and mem[i // 3] + 1 < mem[i] :
        mem[i] = mem[i // 3] + 1
        prev = i // 3
        
    if i % 2 == 0 and mem[i // 2] + 1 < mem[i] :
        mem[i] = mem[i // 2] + 1
        prev = i // 2
        
    path[i] = str(i) + " " + path[prev]
    
print(mem[n])
print(path[n]) 
        