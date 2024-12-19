def solution(n,words):
    w_s=set()
    w_s.add(words[0])
    for i in range(1,len(words)):
        if (words[i]in w_s) or (words[i-1][-1]!=words[i][0]):
            return [(i%n)+1,(i//n)+1]
        w_s.add(words[i])
    return [0,0]