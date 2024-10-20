def solution(num_list, n):
    answer = [[0]*n for _ in range(len(num_list)//n)]
    cnt=0
    j=0
    for i in range(len(num_list)):
        while (j<len(num_list)//n):
            if cnt==n:
                cnt=0
                j+=1
                continue
            else:
                answer[j][cnt]=num_list[i]
                cnt+=1
                break
    return answer