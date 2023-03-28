K, N = map(int, input().split())
L = [int(input()) for _ in range(K)]
L.sort()
st, en = 1, L[K-1]
result = 0

while st <= en:
    mid = (st + en) // 2
    cnt = 0
    for length in L:
        cnt += length // mid

    if cnt < N:
        en = mid - 1
    else:
        st = mid + 1
        result = mid

print(result)