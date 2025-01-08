def solution(s):
    cnt=dict()
    s=s.replace("{","").replace("}","").split(",")
    for i in s:
        i=int(i)
        if i in cnt:
            cnt[i]+=1
        else:
            cnt[i]=1
    answer=sorted(cnt,key=lambda x: cnt[x], reverse=True)
    return answer