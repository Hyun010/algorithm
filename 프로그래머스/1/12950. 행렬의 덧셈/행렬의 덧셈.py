def solution(arr1, arr2):
    answer = [[0]*len(arr1[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            answer[i][j]=arr1[i][j]+arr2[i][j]
    return answer
# #list를 곱셈으로 복사->다 같은 주소값=>첫번째 줄의 0번째 바뀌어도 아래줄 0번째 값 모두 바뀜
# def solution(arr1, arr2):
#     answer = [[0]*len(arr1[0])]*len(arr1)
#     print(answer)
#     for i in range(len(arr1)):
#         for j in range(len(arr1[i])):
#             answer[i][j]=arr1[i][j]+arr2[i][j]
#             continue
#     return answer