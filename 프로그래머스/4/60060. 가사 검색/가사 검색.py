from collections import defaultdict

class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.count = 0 #현재 노드에서 끝나는 단어 개수
    def insert(self, word):
        node = self
        for char in word:
            node = node.children[char]
            node.count += 1 #현재 노드를 지나간 단어 개수 증가
    def search(self, query):
        node = self
        for char in query:
            if char == '?': #와일드카드가 나오면 현재까지 지나온 단어 개수 반환
                return node.count
            if char not in node.children:
                return 0 #매칭되는 단어가 없음
            node = node.children[char]
        return node.count #정확히 끝나는 단어 개수 반환

def solution(words, queries):
    #Trie를 길이별로 저장 (정방향, 역방향)
    tries = defaultdict(Trie) #정방향 Trie
    reversed_tries = defaultdict(Trie) #역방향 Trie
    #길이별 단어 개수 저장 (쿼리가 ?로만 이루어진 경우 빠르게 찾기 위함)
    word_count_by_length = defaultdict(int)
    for word in words:
        length = len(word)
        tries[length].insert(word) #정방향 삽입
        reversed_tries[length].insert(word[::-1]) #역방향 삽입
        word_count_by_length[length] += 1 #길이별 단어 개수 저장
    answer = []
    for query in queries:
        length = len(query)
        #쿼리가 전부 '?'로만 이루어진 경우, 해당 길이의 단어 개수 반환
        if query[0] == '?' and query[-1] == '?':
            answer.append(word_count_by_length[length])
        elif query[0] != '?': #접두사 검색 (정방향 Trie)
            answer.append(tries[length].search(query))
        else: #접미사 검색 (역방향 Trie)
            answer.append(reversed_tries[length].search(query[::-1]))
    return answer
