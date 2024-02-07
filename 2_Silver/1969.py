import sys, collections
input = sys.stdin.readline

gene = []
result=[]

nucleotide = ['A','C','G','T']

n,m = map(int,input().split())
for _ in range(n) :
  gene.append(list(input().rstrip()))


for i in range(m) :
  gene_part = []
  for j in range(n) :
    gene_part.append(gene[j][i])
  
  cnt = []
  
  for j in range(4) :   
    cnt.append(gene_part.count(nucleotide[j]))
  
  if cnt.index(max(cnt)) == 0 :
    result.append('A')
  elif cnt.index(max(cnt))== 1 :
    result.append('C')
  elif cnt.index(max(cnt)) == 2 :
    result.append('G')
  elif cnt.index(max(cnt)) == 3 :
    result.append('T')


print("".join(result))
result_cnt = 0

for i in range(n):
  for j in range(m) :
    if gene[i][j] != result[j] :
      result_cnt += 1

print(result_cnt)


    




