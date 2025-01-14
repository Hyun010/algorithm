def solution(k, dungeons):
    answer = -1
    def rec(c,k,ds): #중첩함수 c: 갯수, k: 피로도, ds 던전 필요,사용
        nonlocal answer #중첩함수 내부에서 외부에도 유지할 수 있게 설정
        for i,d in enumerate(ds):
            if k>=d[0]: #필요 필로도 이상일 때
                nds=ds.copy() #던전 카피 다른 조건을 확인하기 위해 
                nds.pop(i)
                count=rec(c+1,k-d[1],nds)
                if answer<count:
                    answer=count
        return c
    rec(0,k,dungeons)
    return answer