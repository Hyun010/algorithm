def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수 아님
    return True

def solution(nums):
    answer = 0
    all_list=[] #만들 수 있는 전체 리스트
    #만들 수 있는 전체 리스트 반복문(개수가 50개 이하라서 3중 포문 가능)
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                all_list.append(nums[i]+nums[j]+nums[k])
    for i in all_list:
        if is_prime_number(i):
            answer+=1
    return answer