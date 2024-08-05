def solution(files):
    answer = []
    for f in files: #구분하기
        head,number,tail='','','' #기본 포맷 셋팅
        number_check=False #숫자 체크 초기화
        for i in range(len(f)):
            if f[i].isdigit(): #나눈 것들 중 숫자 구분해서 NUMBER에담기
                number+=f[i] #NUMBER 추가
                number_check=True # 숫자 존재 확인
            elif not number_check: #숫자 전 HEAD 추가
                head+=f[i] #HEAD 추가
            else:
                tail=f[i:] #나머지 추가
                break
        answer.append((head,number,tail)) #튜플로 저장
    answer.sort(key=lambda x: (x[0].upper(), int(x[1]))) #HEAD 사전순, 숫자를 이차로 정렬
    answer=[''.join(i) for i in answer] #문자 합쳐서 배열로 만들기
    return answer