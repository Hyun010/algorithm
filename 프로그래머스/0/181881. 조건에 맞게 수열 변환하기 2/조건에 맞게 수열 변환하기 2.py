def solution(arr):  
    answer=0  
    temp=arr  
    while True:  
        temp_s=[]  
        for i in temp:  
            if i>=50 and i%2==0:  
                temp_s.append(i//2)  
            elif i<50 and i%2==1:  
                temp_s.append(i*2+1)  
            else:  
                temp_s.append(i)  
        if temp_s==temp:  
            break  
        answer+=1  
        temp=temp_s  
    return answer
# 복사가 이루져서 작동이 안된다
# def solution(arr):
#     answer = 0
#     temp=[]
#     if len(arr)!=0:
#         while temp!=arr:
#             temp=arr
#             for num in arr:
#                 if num>=50:
#                     if num%2==0:
#                         num=num//2
#                     else:
#                         pass
#                 elif num<50:
#                     if num%2==1:
#                         num=num*2+1
#                     else:
#                         pass
#                 answer+=1
#         answer-=1
#     return answer