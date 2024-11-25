def permutations_2(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in permutations_2(array[:i]+array[i+1:], r-1):
                yield [array[i]] + next

def solution(spell, dic):
    temp=[]
    for i in permutations_2(spell,len(spell)):
        temp.append(''.join(i))
    for t in temp:
        if t in dic:
            print(t)
            return 1
    return 2
