import re
def solution(my_string):
    answer = 0
    num=re.sub(r'[^0-9]','',my_string)
    for n in num:
        answer+=int(n)
    return answer