def solution(new_id):
    #1단계 대문자->소문자
    new_id=new_id.lower()
    #2단계 알파벳 소문자, 숫자, -, _, . 제외한 모든 문자 제거
    valid=set("abcdefghijklmnopqrstuvwxyz01234567890-_.")
    new_id=''.join(c for c in new_id if c in valid)
    #3단계 . 2번이상 연속된 부분 1개의 .로 치환
    while ".." in new_id:
        new_id=new_id.replace("..",'.')
    #4단계 . 처음이나 끝 제거
    new_id=new_id.strip('.')
    #5단계 빈문자열이라면 new_id->a 대입
    if not new_id:
        new_id="a"
    #6단계 길이 16이상->처음 15자 제외한 나머지 제거, 끝 . 제거
    if len(new_id)>15:
        new_id=new_id[:15].rstrip('.')
    #7단계 길이 2자 이하 마지막 문자 길이 3될 때까지 반복해서 끝에 붙이기
    while len(new_id)<3:
        new_id+=new_id[-1]
    return new_id