def solution(participant, completion):
    participant.sort() #순서 맞추기 정렬
    completion.sort() #순서 맞추기 정렬
    for p,c in zip(participant,completion): #zip으로 묶어서 확인
        if p!=c: #같지 않으면 완주 못한 사람
            return p #완주 못한 참가자 리턴
    return participant[-1] #확인 다하고 남은 마지막 사람이 완주 못한사람