def solution(record):
    answer = [] #출력 정보
    user={} #유저 정보DB
    record=[i.split(' ') for i in record] #공백 기준 나누기
    for i in record: #닉네임 변경 설정 먼저 해주기
        if (i[0]=='Change' and i[1] in user): #유저 정보가 들어가 있고 첫 단어가 Change면 닉네임 변경
            user[i[1]]=i[2] #새로운 닉네임
        elif (i[0]=='Enter' and i[1] in user) or (i[0]=='Enter' and i[1] not in user): #유저가 등록되었든 안되었든 들어오는 것은 닉네임 설정
            user[i[1]]=i[2] #새로운 닉네임
    for i in record: #출력 설정해주기
        if i[0]=='Enter': #들어오는 것
            answer.append('%s님이 들어왔습니다.' %user[i[1]])
        elif i[0]=='Leave': #나가는 것
            answer.append('%s님이 나갔습니다.' %user[i[1]])
    return answer