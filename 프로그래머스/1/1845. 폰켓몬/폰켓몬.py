def solution(nums):
    kind=len(set(nums))
    catch=len(nums)//2
    answer=min(kind,catch)
    return answer