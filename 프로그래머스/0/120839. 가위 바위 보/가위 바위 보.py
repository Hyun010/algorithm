def solution(rsp):
    answer = ''
    str=rsp.maketrans('205','052')
    answer=rsp.translate(str)
    return answer