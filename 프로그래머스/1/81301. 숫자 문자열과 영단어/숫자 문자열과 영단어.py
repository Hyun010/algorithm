def solution(s):
    check={'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9','zero':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','0':'0'}
    answer = ''
    t=''
    for i in range(len(s)):
        if s[i].isdigit():
            answer+=s[i]
        else:
            t+=s[i]
        if t in check:
            answer+=check[t]
            t=''
    return int(answer)