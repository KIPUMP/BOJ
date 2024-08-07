import sys
from collections import defaultdict

# 빠른 입력을 위해 sys.stdin.readline을 사용합니다.
input = sys.stdin.readline

# Trie의 각 노드를 나타내는 클래스입니다.
class Node:
    def __init__(self):
        self.word = False  # 이 노드가 단어의 끝을 나타내는지 여부를 저장합니다.
        self.children = {} # 자식 노드들을 저장하는 딕셔너리입니다.

# Trie 자료구조를 관리하는 클래스입니다.
class Trie:
    def __init__(self):
        self.root = Node()  # 트라이의 루트 노드를 초기화합니다.

    # 단어를 트라이에 삽입하는 함수입니다.
    def insert(self, word):
        node = self.root  # 루트 노드부터 시작합니다.
    
        # 단어의 각 문자에 대해
        for char in word:
            # 해당 문자가 자식 노드에 없다면 새로운 노드를 만듭니다.
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]  # 자식 노드로 이동합니다.
        
        # 같은 닉네임의 횟수를 증가시킵니다.
        same_nick[word] += 1
        node.word = True  # 이 노드가 단어의 끝임을 표시합니다.

    # 트라이에서 단어를 검색하여 적절한 닉네임을 반환하는 함수입니다.
    def search(self, word):
        node = self.root  # 루트 노드부터 시작합니다.
        re_word = ''      # 결과 닉네임을 저장할 변수입니다.
        
        # 단어의 각 문자에 대해
        for char in word:
            re_word += char  # 결과 닉네임에 문자를 추가합니다.
            # 해당 문자가 자식 노드에 없다면 결과 닉네임을 반환합니다.
            if char not in node.children:
                return re_word
            node = node.children[char]  # 자식 노드로 이동합니다.
        
        # 노드가 단어의 끝을 나타낸다면
        if node.word:
            # 같은 닉네임의 수에 +1을 하여 결과 닉네임에 추가합니다.
            re_word += str(same_nick[re_word] + 1)
        
        return re_word

# 입력된 단어의 개수를 나타냅니다.
n = int(input())
tree = Trie()  # 트라이를 초기화합니다.
same_nick = defaultdict(int)  # 같은 닉네임의 수를 저장할 딕셔너리를 초기화합니다.

# n개의 단어를 처리합니다.
for _ in range(n):
    word = input().rstrip()  # 입력된 단어에서 공백을 제거합니다.
    print(tree.search(word))  # 트라이에서 적절한 닉네임을 검색하여 출력합니다.
    tree.insert(word)  # 트라이에 단어를 삽입합니다.
