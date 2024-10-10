def calculate(a, b, operator): #연산자 따라 계산
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b

def evaluate_expression(numbers, operators, precedence): #우선순위 따라 계산
    for operator in precedence:
        i = 0
        while i < len(operators):
            if operators[i] == operator: #발견시 계산
                result = calculate(numbers[i], numbers[i + 1], operator)
                numbers[i] = result #업데이트
                del numbers[i + 1] #삭제
                del operators[i] #삭제
            else: #발견X 다음 수로 넘어가기
                i += 1  
    return abs(numbers[0]) #최종 계산은 절대값처리

def solution(expression):
    numbers = []
    operators = []
    num = ''
    answer = 0
    
    for char in expression: #숫자와 연산자 분리
        if char.isdigit():
            num += char
        else:
            numbers.append(int(num))
            operators.append(char)
            num = ''
    
    numbers.append(int(num)) #마지막 숫자 추가
    #연산자 우선순위 조합 만들기
    precedence_list = [
        ['+', '-', '*'],
        ['+', '*', '-'],
        ['-', '+', '*'],
        ['-', '*', '+'],
        ['*', '+', '-'],
        ['*', '-', '+']
    ]
    for precedence in precedence_list: #우선순위에 따른 조합 중 가장 큰 값
        current_numbers = numbers[:]
        current_operators = operators[:]  
        result = evaluate_expression(current_numbers, current_operators, precedence)
        answer = max(answer, result)
    return answer