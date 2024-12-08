def solution(s, n):
    p = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    p2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    answer = []
    s=list(s)
    for str in s:
        if str in p:
            idx=(p.index(str)+n)%26
            answer.append(p[idx])
        elif str in p2:
            idx2=(p2.index(str)+n)%26
            answer.append(p2[idx2])
        elif str==' ':
            answer.append(' ')
    answer=''.join(answer)
    return answer