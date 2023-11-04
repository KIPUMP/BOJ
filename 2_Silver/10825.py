n = int(input())
students = []
for _ in range(n) :
    name,korean,english,math = input().split()
    students.append((name,korean,english,math))
    
students = sorted(students, key = lambda x : (-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for i in students :
    print(i[0])