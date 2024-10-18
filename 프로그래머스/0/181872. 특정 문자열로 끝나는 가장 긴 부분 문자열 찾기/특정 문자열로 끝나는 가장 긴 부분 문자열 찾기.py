def solution(myString, pat):
    answer = ''
    temp=''
    tmp_pat=''
    tmp_pat=pat[::-1]
    temp+=myString[::-1]
    s=temp.find(tmp_pat)
    answer=temp[s:]
    answer=answer[::-1]
    return answer