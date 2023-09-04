for _ in range(int(input())) :
  N = int(input())
  resumes = []
  total = N
  for _ in range(N):
    first_test,second_test = map(int,input().split())
    resumes.append((first_test,second_test))
  resumes.sort()
  print(resumes)
  for j in range(N) :
    t = 0
    for i in range(len(resumes)-1) :
      if resumes[t][0] < resumes[(-1)][0] and resumes[t][1] < resumes[(-1)][1] :
        resumes.remove(resumes[(-1)])
        total -= 1
        break

  
  print(total)

  
