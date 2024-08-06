class TrieNode:
    def __init__(self):
        # 각 Trie 노드는 자식 노드에 대한 빈 딕셔너리와 카운터를 초기화합니다.
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        # Trie의 루트는 빈 TrieNode입니다.
        self.root = TrieNode()
        
    def insert(self, name):
        # Trie의 루트부터 시작합니다.
        current = self.root
        # 이름에 대한 고유 접두사를 저장할 변수입니다.
        unique_prefix = ""
        
        # 이름의 각 문자에 대해 반복합니다.
        for char in name:
            # 현재 문자를 접두사에 추가합니다.
            unique_prefix += char
            # 현재 노드의 자식에 문자가 없으면 추가합니다.
            if char not in current.children:
                current.children[char] = TrieNode()
            
            # 자식 노드로 이동합니다.
            current = current.children[char]
            # 현재 노드의 카운트를 증가시킵니다.
            current.count += 1

            # 현재 노드의 카운트가 1이면, 고유 접두사를 찾은 것입니다.
            if current.count == 1:
                return unique_prefix
        
        # 모든 접두사가 이미 사용 중인 경우, 이름에 카운트를 접미사로 추가하여 반환합니다.
        return name + str(current.count)
    
def generate_nicknames(names):
    # Trie와 닉네임을 저장할 리스트를 초기화합니다.
    trie = Trie()
    nicknames = []
    
    # 각 이름을 처리합니다.
    for name in names:
        # Trie에 이름을 삽입하고 닉네임을 얻습니다.
        nickname = trie.insert(name)
        # 결과 리스트에 닉네임을 추가합니다.
        nicknames.append(nickname)
    
    return nicknames

def main():
    import sys
    input = sys.stdin.readline
    
    # 이름의 수를 읽습니다.
    n = int(input())
    # 각 이름을 리스트에 저장합니다.
    names = [input().strip() for _ in range(n)]
    
    # 고유 닉네임을 생성합니다.
    nicknames = generate_nicknames(names)
    
    # 각 닉네임을 출력합니다.
    for nickname in nicknames:
        print(nickname)

if __name__ == "__main__":
    main()
