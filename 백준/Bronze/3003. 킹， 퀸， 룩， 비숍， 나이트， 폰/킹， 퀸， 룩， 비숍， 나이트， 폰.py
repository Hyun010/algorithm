k, q, l, s, n, p = map(int, input().split())
standard = [1, 1, 2, 2, 2, 8]
need = [s - c for s, c in zip(standard, [k, q, l, s, n, p])]
print(*need)