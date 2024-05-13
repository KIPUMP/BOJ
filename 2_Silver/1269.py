import sys
input = sys.stdin.readline

a,b = map(int,input().split())

a_arr = set(map(int,input().split()))
b_arr = set(map(int,input().split()))

print(len(a_arr-b_arr) + len(b_arr-a_arr))

