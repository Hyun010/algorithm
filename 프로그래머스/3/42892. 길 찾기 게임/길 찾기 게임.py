import sys
sys.setrecursionlimit(10**6)

class TreeNode:
    def __init__(self, y, x, idx):
        self.y = y
        self.x = x
        self.idx = idx
        self.left = None
        self.right = None

#이진 트리 삽입 함수
def insert(node, tree):
    if tree is None:
        return node
    if node.x < tree.x: #왼쪽 서브트리
        tree.left = insert(node, tree.left)
    else: #오른쪽 서브트리
        tree.right = insert(node, tree.right)
    return tree
             
def solution(nodeinfo):
    #노드 정보 만들기
    nodes = [(y, x, idx + 1) for idx, (x, y) in enumerate(nodeinfo)]
    nodes.sort(reverse=True) #y값 기준 내림차순
    root = None
    #트리 구성
    for node in nodes:
        new_node = TreeNode(node[0], node[1], node[2])
        root = insert(new_node, root)
    preorder_result = []
    postorder_result = []
    #전위 순회 함수
    def preorder(node):
        if node is None:
            return
        preorder_result.append(node.idx) #노드 번호 추가
        preorder(node.left) #왼쪽 서브트리
        preorder(node.right) #오른쪽 서브트리

    #후위 순회 함수
    def postorder(node):
        if node is None:
            return
        postorder(node.left) #왼쪽 서브트리
        postorder(node.right) #오른쪽 서브트리
        postorder_result.append(node.idx) #노드 번호 추가
    #전위 순회 및 후위 순회 실행
    preorder(root)
    postorder(root)
    return [preorder_result, postorder_result]