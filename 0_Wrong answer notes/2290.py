def create_segment(size, top, middle, bottom, top_left, top_right, bottom_left, bottom_right):
    segment = []
    segment.append(" " + top * size + " ")
    for _ in range(size):
        segment.append(top_left + " " * size + top_right)
    segment.append(" " + middle * size + " ")
    for _ in range(size):
        segment.append(bottom_left + " " * size + bottom_right)
    segment.append(" " + bottom * size + " ")
    return segment


import sys
input = sys.stdin.readline
data = input().split()

s = int(data[0])
n = data[1]

segments = [
    create_segment(s, "-", " ", "-", "|", "|", "|", "|"), # 0
    create_segment(s, " ", " ", " ", " ", "|", " ", "|"), # 1
    create_segment(s, "-", "-", "-", " ", "|", "|", " "), # 2
    create_segment(s, "-", "-", "-", " ", "|", " ", "|"), # 3
    create_segment(s, " ", "-", " ", "|", "|", " ", "|"), # 4
    create_segment(s, "-", "-", "-", "|", " ", " ", "|"), # 5
    create_segment(s, "-", "-", "-", "|", " ", "|", "|"), # 6
    create_segment(s, "-", " ", " ", " ", "|", " ", "|"), # 7
    create_segment(s, "-", "-", "-", "|", "|", "|", "|"), # 8
    create_segment(s, "-", "-", "-", "|", "|", " ", "|")  # 9
]

row_count = 2 * s + 3
result = [""] * row_count

for row in range(row_count):
    line = []
    for digit in n:
        line.append(segments[int(digit)][row])
    result[row] = " ".join(line)
    
for line in result:
    print(line)

