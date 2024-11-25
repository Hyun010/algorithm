#유일성
def is_unique(relation, bitmask):
    seen = set()
    for row in relation:
        key = tuple(row[i] for i in range(len(row)) if bitmask & (1 << i))
        seen.add(key)
    return len(seen) == len(relation)

#최소성
def is_minimal(candidate_keys, bitmask):
    for existing in candidate_keys:
        print(existing, bitmask)
        if existing & bitmask == existing:
            return False
    return True

def solution(relation):
    num_columns = len(relation[0]) #컬럼수
    candidate = [] #후보키 배열
    for bitmask in range(1, 1 << num_columns):
        if is_unique(relation, bitmask) and is_minimal(candidate, bitmask):
            candidate.append(bitmask)
    return len(candidate)