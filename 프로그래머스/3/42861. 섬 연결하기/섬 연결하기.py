#부모 노드 찾기
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x]) #최종 부모 찾기
    return parent[x]

#경로 합치기
def union(parent, rank, x, y):
    rootX = find(parent, x) #최종 뿌리
    rootY = find(parent, y) #최종 뿌리
    
    if rootX != rootY: #뿌리가 다르면 경로 이동 합치기
        if rank[rootX] > rank[rootY]: #우선순위에 따라 합치기
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else: #처음 시작(우선순위) 채우기
            parent[rootY] = rootX
            rank[rootX] += 1

def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]
    rank = [0] * n
    costs.sort(key=lambda x: x[2]) #비용 기준 오름차순 정렬
    for cost in costs:
        u, v, c = cost #코스트 파싱
        if find(parent, u) != find(parent, v): #부모가 다르면 합치기
            union(parent, rank, u, v) #섬 합치기
            answer += c #비용추가
    return answer