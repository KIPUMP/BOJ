n = int(input())

enter_list = {}
for i in range(n) : 
    name, behavior = map(str,input().split())
    if behavior == 'enter' :
        enter_list[name] = behavior
    else:
        del enter_list[name]
        
enter_list = sorted(enter_list,reverse=True)

for i in enter_list :
    print(i)
