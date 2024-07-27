class Node :
    def __init__(self,item,left,right) :            # 간선 연결
        self.item = item                            # 부모
        self.left = left                            # 왼쪽
        self.right = right                          # 오른쪽
        
# 부모노드가 '.' 값이 아니면 재귀를 통해 순회한다.
def preorder(node) :                                # 전위 순회(재귀 앞에 출력)
    print(node.item,end="")                         
    if node.left != '.' :
        preorder(tree[node.left])
    if node.right != '.' :
        preorder(tree[node.right])
        
def inorder(node) :                                 # 중위 순회(재귀 중간에 출력)
    if node.left != '.' :                           
        inorder(tree[node.left])
    print(node.item, end="")                
    if node.right != '.' :
        inorder(tree[node.right])
        
def postorder(node) :                               # 후위 순회(재귀 후에 출력)
    if node.left != '.' :
        postorder(tree[node.left])
    if node.right != '.' :
        postorder(tree[node.right])
    print(node.item, end="")
    
n = int(input())
inputs = []
for _ in range(n):
    inputs.append(input().split())

tree = {}

for item, left, right in inputs:
    tree[item] = Node(item, left, right)
    
preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])
 