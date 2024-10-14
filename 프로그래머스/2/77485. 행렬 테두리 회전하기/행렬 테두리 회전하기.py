def solution(rows, columns, queries):
    answer = []

    matrix = [[(i * columns) + j + 1 for j in range(columns)] for i in range(rows)] #행렬 생성
    
    for query in queries:
        x1, y1, x2, y2 = query #쿼리 초기화
        border = [] #테두리 리스트
        #테두리 숫자 저장
        for j in range(y1 - 1, y2): #상단
            border.append(matrix[x1 - 1][j])
        for i in range(x1, x2): #우측
            border.append(matrix[i][y2 - 1])
        for j in range(y2 - 2, y1 - 2, -1): #하단
            border.append(matrix[x2 - 1][j])
        for i in range(x2 - 2, x1 - 1, -1): #좌측
            border.append(matrix[i][y1 - 1])
        border.insert(0, border.pop()) #회전
        idx = 0 #테두리 숫자 인덱스
        #행렬에 테두리 다시 삽입
        # 상단
        for j in range(y1 - 1, y2):
            matrix[x1 - 1][j] = border[idx]
            idx += 1
        # 우측
        for i in range(x1, x2):
            matrix[i][y2 - 1] = border[idx]
            idx += 1
        # 하단
        for j in range(y2 - 2, y1 - 2, -1):
            matrix[x2 - 1][j] = border[idx]
            idx += 1
        # 좌측
        for i in range(x2 - 2, x1 - 1, -1):
            matrix[i][y1 - 1] = border[idx]
            idx += 1
        answer.append(min(border)) #회전 후 테두리 중 가장 작은 수 저장
    return answer