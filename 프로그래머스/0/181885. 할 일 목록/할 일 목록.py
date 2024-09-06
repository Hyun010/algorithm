def solution(todo_list, finished):
    answer = []
    for i, b in enumerate(finished):
        if b==False:
            answer.append(todo_list[i])
    return answer