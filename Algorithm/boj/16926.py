N, M, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

for r in range(R):
    for i in range(min(N, M) // 2):
        y, x = i, i
        temp = A[i][i]
        # 오른쪽으로
        for j in range(i, M-i-1):
            x = j
            A[y][x] = A[y][x+1]
        x += 1
        # 아래로
        for j in range(i, N-i-1):
            y = j
            A[y][x] = A[y+1][x]
        y += 1
        # 왼쪽으로
        for j in range(M-i-1, i, -1):
            x = j
            A[y][x] = A[y][x-1]
        x -= 1
        # 위로
        for j in range(N-i-1, i, -1):
            y = j
            A[y][x] = A[y-1][x]
        A[i+1][i] = temp

for a in A:
    print(*a)
