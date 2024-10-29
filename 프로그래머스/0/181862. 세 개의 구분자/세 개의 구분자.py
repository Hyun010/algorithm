import re

def solution(myStr):
    answer = []
    answer=re.split('[a|b|c]',myStr)
    answer = ' '.join(answer).split()
    if answer==[]:
        answer.append('EMPTY')
    return answer