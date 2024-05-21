d,h,w = map(int,input().split())


ratio = d /((h**2 + w **2) ** 0.5)

height = int(h*ratio)
area = int(w*ratio)

print(height, area)

