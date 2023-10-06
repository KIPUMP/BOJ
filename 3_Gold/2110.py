n,c = map(int,input().split())
home = []
for _ in range(n) :
  home.append(int(input()))

home.sort()

start = home[0]
end = home[-1]

wifi = (start + end) // 2
for i in range(n) :
  if wifi - 1  <= home[i] <= wifi + 1 :
    home[i]

  