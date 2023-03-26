# (0, 0) -> (N-1, N-1)까지 최소로 이동
from heapq import heappush, heappop


INF = float('inf')
tc = 1
while True:
    N = int(input())

    if not N:
        break

    result = [[INF]*N for _ in range(N)]
    cave = [list(map(int, input().split())) for _ in range(N)]

    result[0][0] = 0
    hq = [(cave[0][0], (0, 0))]
    while hq:
        cost, (y, x) = heappop(hq)
        for (dy, dx) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < N:
                c = cost + cave[ny][nx]
                if c < result[ny][nx]:
                    result[ny][nx] = c
                    heappush(hq, (c, (ny, nx)))

    print('Problem ' + str(tc) + ': ' + str(result[N-1][N-1]))
    tc += 1