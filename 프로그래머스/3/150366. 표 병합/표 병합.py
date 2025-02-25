class Table:
    def __init__(self):
        self.parent = {(r, c): (r, c) for r in range(1, 51) for c in range(1, 51)}
        self.table = {}

    def find(self, cell):
        """대표 노드를 찾는 유니온-파인드 (경로 압축)"""
        if self.parent[cell] != cell:
            self.parent[cell] = self.find(self.parent[cell])
        return self.parent[cell]

    def union(self, cell1, cell2):
        """셀 병합 (값이 있는 셀의 값을 유지)"""
        root1, root2 = self.find(cell1), self.find(cell2)
        if root1 == root2:
            return  # 이미 같은 그룹이면 병합 필요 없음
        
        # 기존 값 가져오기
        val1 = self.table.get(root1, None)
        val2 = self.table.get(root2, None)

        # 작은 좌표를 기준으로 병합
        if root1 > root2:
            root1, root2 = root2, root1

        # 병합 (대표 노드 설정)
        self.parent[root2] = root1

        # 값 결정: 값이 있는 쪽을 유지
        if val1 is None and val2 is not None:
            self.table[root1] = val2
        elif val1 is not None:
            self.table[root1] = val1
        
        # 병합된 노드의 값 삭제 (중복 방지)
        if root2 in self.table:
            del self.table[root2]

    def update_cell(self, r, c, value):
        """특정 셀 값을 변경"""
        root = self.find((r, c))
        self.table[root] = value

    def update_value(self, value1, value2):
        """값을 가진 모든 셀을 변경"""
        for key in list(self.table.keys()):
            if self.table[key] == value1:
                self.table[key] = value2

    def unmerge(self, r, c):
        """셀 병합 해제"""
        root = self.find((r, c))
        value = self.table.get(root, None)

        # 병합된 모든 셀을 원래 상태로 복원
        to_unmerge = [cell for cell in self.parent.keys() if self.find(cell) == root]
        for cell in to_unmerge:
            self.parent[cell] = cell
            if cell in self.table:
                del self.table[cell]

        # 선택된 셀만 값을 유지
        if value is not None:
            self.table[(r, c)] = value

    def print_cell(self, r, c):
        """셀 값 출력"""
        root = self.find((r, c))
        return self.table.get(root, "EMPTY")


def solution(commands):
    table = Table()
    result = []

    for command in commands:
        parts = command.split()
        cmd = parts[0]

        if cmd == "UPDATE":
            if len(parts) == 4:
                r, c, value = int(parts[1]), int(parts[2]), parts[3]
                table.update_cell(r, c, value)
            else:
                value1, value2 = parts[1], parts[2]
                table.update_value(value1, value2)

        elif cmd == "MERGE":
            r1, c1, r2, c2 = map(int, parts[1:])
            table.union((r1, c1), (r2, c2))

        elif cmd == "UNMERGE":
            r, c = map(int, parts[1:])
            table.unmerge(r, c)

        elif cmd == "PRINT":
            r, c = map(int, parts[1:])
            result.append(table.print_cell(r, c))

    return result
