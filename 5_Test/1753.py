import heapq, sys
input = sys.stdin.readline

def dijkstra(graph,start,v) :
  dist = [1e9] * v
  


V,E = map(int,input().split())
K = int(input())
arr = [[] for _ in range(V)]
for i in range(E) :
  u,v,w = map(int,input().split())
  arr[u-1].append((v-1,w))
