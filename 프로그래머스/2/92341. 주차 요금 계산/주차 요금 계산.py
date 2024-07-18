from math import ceil
def solution(fees, records):
    answer = []
    pc={}
    for r in records:
        time=int(r[:2])*60+int(r[3:5]) #5자리 시간을 분으로 해서 통합
        car=r[6:10] #4자리의 차량번호
        if car not in pc.keys(): #차량번호가 없을시 주차 시간, 입출차 시각, 상태를 값으로 한다
            pc[car]=[0, time, 'IN']
        else: #주차장에서 있고 상태 확인
            if r[-2:]=='IN':
                pc[car][1],pc[car][2]=time, 'IN' #입차 상태와 시간 기록
            else:
                pc[car][0]+=time-pc[car][1] #출차이므로 주차시간 구하기
                pc[car][1],pc[car][2]=time, 'OUT' #출차로 상태 바꾸기
    for k,v in pc.items():
        if v[-1]=='IN':
            v[0]+=1439-v[1] #마지막 출차 값으로 더해주기
        f=fees[1] #기본요금
        if v[0]>fees[0]: #기본시간 보다 크면 요금 더해주기
            f+=ceil((v[0]-fees[0])/fees[2])*fees[3]
        answer.append([k,f]) #차량번호와 주차 요금 추가
    answer=sorted(answer) #차량번호 기준 오름차순
    return [value[1] for value in answer] #요금만 보내기