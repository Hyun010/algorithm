#회전
def rotate_key(key):
    M = len(key)
    return [[key[M - 1 - j][i] for j in range(M)] for i in range(M)]

#열리는지 확인
def check(new_lock):
    lock_size = len(new_lock) // 3
    for i in range(lock_size, lock_size * 2):
        for j in range(lock_size, lock_size * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    M, N = len(key), len(lock)
    #자물쇠 3배 확장
    new_lock = [[0] * (N * 3) for _ in range(N * 3)]
    for i in range(N):
        for j in range(N):
            new_lock[N + i][N + j] = lock[i][j]
    for _ in range(4): #본래것까지 확인
        key = rotate_key(key)
        for x in range(1, N * 2):
            for y in range(1, N * 2):
                #열쇠 배치
                for i in range(M):
                    for j in range(M):
                        new_lock[x + i][y + j] += key[i][j]
                #확인
                if check(new_lock):
                    return True
                #열쇠 제거(틀리면 원상복귀)
                for i in range(M):
                    for j in range(M):
                        new_lock[x + i][y + j] -= key[i][j]
    return False