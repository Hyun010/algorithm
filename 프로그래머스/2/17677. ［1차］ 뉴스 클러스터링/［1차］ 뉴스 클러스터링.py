def makelist(str):
    templist=[]
    for i in range(1,len(str)):
        temp=str[i-1]+str[i]
        if temp.isalpha():
            templist.append(temp.lower())
    return templist

def gyohap(list1,list2):
    temp1=[]
    temp2=[]
    for i in (set(list1+list2)):
        j=list1.count(i)
        k=list2.count(i)
        ma=max(j,k)
        mi=min(j,k)
        temp1.append(mi)
        temp2.append(ma)
    return temp1,temp2

def solution(str1, str2):
    answer = 0
    list1=makelist(str1)
    list2=makelist(str2)
    gyo,hap=gyohap(list1,list2)
    if sum(gyo)!=0 and len(hap)!=0:
        answer=int((sum(gyo)/sum(hap))*65536)
    elif sum(gyo)==0 and len(hap)!=0:
        return 0
    else:
        return 65536
    return answer