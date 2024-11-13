def solution(numbers):
    answer = ''
    c=''
    check={"zero":"0",'one':"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
    for i in range(len(numbers)):
        if c in check:
            answer+=check[c]
            c=''
            c+=numbers[i]
        else:
            c+=numbers[i]
    answer+=check[c]
    return int(answer)