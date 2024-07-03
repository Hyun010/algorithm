def solution(msg):
    answer = [0] #사전에 없을 경우 -1 부분을 해결하기 위한 초기화
    dic={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26} #사전 초기화
    s="" #새로운 단어 담을 공간
    g=26 #기본 위치
    for i in range(len(msg)):
        s+=msg[i] #다음 단어 추가
        if not s in dic: #추가한 단어가 사전에 없을 때
            g+=1 #기준 +1
            dic[s]=g #사전에 등록
            s=msg[i] #단어 리셋(1자리)
            answer.append(dic[s]) #1자리에 맞는 색인 번호 등록
        else: #추가한 단어가 사전에 있을 때
            answer[-1]=dic[s] #마지막 번호 변경(사전에 있는 단어로)
    return answer