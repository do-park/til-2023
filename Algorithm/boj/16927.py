from collections import deque


N, M, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
result = [[0]*M for _ in range(N)]

for i in range(min(N, M) // 2):
    y, x = i, i
    q = deque()
    for j in range(i, N-i-1):
        y = j
        q.append(A[y][x])
    y += 1
    for j in range(i, M-i-1):
        x = j
        q.append(A[y][x])
    x += 1
    for j in range(N-i-1, i, -1):
        y = j
        q.append(A[y][x])
    y -= 1
    for j in range(M-i-1, i, -1):
        x = j
        q.append(A[y][x])

    q.rotate(R)
    y, x = i, i
    for j in range(i, N-i-1):
        y = j
        result[y][x] = q.popleft()
    y += 1
    for j in range(i, M-i-1):
        x = j
        result[y][x] = q.popleft()
    x += 1
    for j in range(N-i-1, i, -1):
        y = j
        result[y][x] = q.popleft()
    y -= 1
    for j in range(M-i-1, i, -1):
        x = j
        result[y][x] = q.popleft()

for r in result:
    print(*r)


