def solution(n, k, cmd):
    linked_list = {i: [i - 1, i + 1] for i in range(n)} #연결리스트로 초기화
    linked_list[0][0] = None  #첫 행 이전노드 없음
    linked_list[n - 1][1] = None  #막 행 다음 노드 없음
    stack = [] #삭제행 스택
    current = k #현재 행
    for command in cmd:
        if command.startswith('U'): #위 이동
            x = int(command.split()[1]) #이동 칸
            for _ in range(x):
                current = linked_list[current][0] #이전으로 이동
        elif command.startswith('D'): #아래 이동
            x = int(command.split()[1]) #이동 칸
            for _ in range(x):
                current = linked_list[current][1] #다음으로 이동
        elif command == 'C': #삭제
            prev, next = linked_list[current] #이전, 다음
            stack.append((current, prev, next)) #현재 노드 스택 저장
            if prev is not None: #이전 노드 존재->연결 갱신
                linked_list[prev][1] = next
            if next is not None: #다음 노드 존재->연결 갱신
                linked_list[next][0] = prev
            #다음 행 이동(없으면 이전 행 선택)->마지막 행일 경우
            current = next if next is not None else prev
        elif command == 'Z': #복구
            row, prev, next = stack.pop() #복구행 정보 가져오기
            if prev is not None: #이전 노드 존재->연결 복구
                linked_list[prev][1] = row
            if next is not None: #다음 노드 존재->연결 복구
                linked_list[next][0] = row
    result = ['O'] * n #기본 존재
    for row, _, _ in stack: #삭제된 현재 행->X 처리
        result[row] = 'X'
    return ''.join(result)