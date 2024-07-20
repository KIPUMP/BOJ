file_dict = {}

for _ in range(int(input())) :
    file_name = input().split('.')
    

    if file_name[1] in file_dict :
        file_dict[file_name[1]] += 1

    else :
        file_dict[file_name[1]] = 1

file_dict = sorted(file_dict.items(), key= lambda x : x[0])

for i in file_dict :
    print(i[0],i[1])
