from collections import deque


N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
result = 0

while True:
    q = deque()
    visited = [[False for _ in range(N)] for _ in range(N)]
    flag = N*N

    for r in range(N):
        for c in range(N):
            if visited[r][c]:
                continue

            flag -= 1
            q.append((r, c))
            visited[r][c] = True
            unioned = [(r, c)]
            total, cnt = A[r][c], 1

            while q:
                (y, x) = q.popleft()
                for (dy, dx) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and L <= abs(A[y][x] - A[ny][nx]) <= R:
                        q.append((ny, nx))
                        visited[ny][nx] = True
                        unioned.append((ny, nx))
                        total += A[ny][nx]
                        cnt += 1

            ave = total // cnt
            for (y, x) in unioned:
                A[y][x] = ave

    if not flag:
        print(result)
        break

    result += 1
