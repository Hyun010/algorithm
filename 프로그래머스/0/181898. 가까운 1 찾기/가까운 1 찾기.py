def solution(arr, idx):
    try:
        answer=arr.index(1,idx)
    except:
        answer=-1
    return answer