class TrieNode:
    def __init__(self):
        self.children = {} #자식 노드 저장 (dict 형태)
        self.count = 0 #이 지점까지 온 단어의 개수

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """ 단어를 Trie에 삽입하면서 각 노드에 방문한 횟수를 기록 """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1 #해당 노드를 거치는 단어 개수 증가

    def count_typing(self, word):
        """ 단어를 검색할 때, 몇 글자를 입력해야 하는지 계산 """
        node = self.root
        typing_count = 0
        for char in word:
            typing_count += 1
            node = node.children[char]
            if node.count == 1: #더 이상 다른 단어와 공유되지 않으면 중단
                break
        return typing_count

def solution(words):
    trie = Trie()

    #Trie에 모든 단어 삽입
    for word in words:
        trie.insert(word)

    #모든 단어에 대해 최소 입력 문자 개수 계산
    return sum(trie.count_typing(word) for word in words)
