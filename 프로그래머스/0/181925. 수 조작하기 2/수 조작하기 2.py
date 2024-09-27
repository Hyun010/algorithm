def solution(numLog):
    answer = ''
    for i in range(len(numLog)):
        if (i+1)<=len(numLog)-1:
            if abs(numLog[i]-numLog[i+1])==1:
                if (numLog[i]-numLog[i+1])<0:
                    answer+='w'
                else:
                    answer+='s'
            elif abs(numLog[i]-numLog[i+1])==10:
                if (numLog[i]-numLog[i+1])<0:
                    answer+='d'
                else:
                    answer+='a'
            continue
        else:
            break           
    return answer