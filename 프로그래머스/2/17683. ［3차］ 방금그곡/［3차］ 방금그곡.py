#문자열로 나타내기 위해 소문자변환
def change_lower(mel):
    return mel.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a').replace('B#','b')

#플레이시간에 맞는 음악만들기
def get_melody(s,e,sh):
    start_h,start_m=map(int,s.split(':')) #시작 파싱
    end_h,end_m=map(int,e.split(':')) #끝 파싱
    played=(end_h*60+end_m)-(start_h*60+start_m) #플레이시간(분)
    full=(sh*(played//len(sh)))+sh[:played%len(sh)]
    return full

def solution(m,musicinfos):
    m=change_lower(m) #기억한 멜로디 # 소문자 변환
    answer=''
    max_pt=0 #오래 재생된 음악시간
    
    for i in musicinfos:
        start,end,title,s=i.split(',') #정보 파싱
        s=change_lower(s) #악보 # 소문자 변환
        played_m=get_melody(start,end,s) #음악 만들기
        
        if m in played_m: #기억한 멜로디가 재생된 멜로디에 존재할 경우
            played_time=len(played_m) #재생된 전체 시간
            if played_time>max_pt: #더 긴 재생 시간 찾으면 업데이트
                answer=title
                max_pt=played_time
    if answer=='': #비었으면 None 반환
        return "(None)"
    return answer