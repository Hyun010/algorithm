def solution(data, ext, val_ext, sort_by):
    answer = []
    for item in data: #ext와 val_ext 비교->작은것
        if ext == "code" and item[0] < val_ext:
            answer.append(item)
        elif ext == "date" and item[1] < val_ext:
            answer.append(item)
        elif ext == "maximum" and item[2] < val_ext:
            answer.append(item)
        elif ext == "remain" and item[3] < val_ext:
            answer.append(item)
    sort_index = {"code": 0, "date": 1, "maximum": 2, "remain": 3} #정렬 기준
    answer.sort(key=lambda x: x[sort_index[sort_by]]) #기준에 따른 정렬
    return answer