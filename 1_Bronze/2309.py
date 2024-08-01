dwarfs = []

def solution(arr, sub_val) :
    for i in range(len(arr)) :
        for j in range(i) :
            if arr[i] + arr[j] == sub_val :
                arr.remove(arr[i])
                arr.remove(arr[j])
                return arr 
            
for _ in range(9) :
    dwarfs.append(int(input()))

# 난쟁이 키의 차(7 난쟁이가 아닌 2 난쟁이 키의 합)
sub_val = sum(dwarfs) - 100    

result = solution(dwarfs,sub_val) 

result.sort()

for i in result :
    print(i)


# 31120	40

