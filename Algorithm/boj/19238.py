# 스타트 택시
# 손님을 도착지로 데려다 줄 때마다 연료가 충전, 연료가 바닥나면 그 날의 업무가 끝난다.
# N * N 크기의 격자, 상하좌우, 최단경로
# M명의 승객
# 현재 위치에서 최단거리가 가장 짧은 승객을 고른다. 여러 명이면 행 번호가 가장 작은 승객, 열 번호가 가장 작은 승객
# 연료는 한 칸 이동할 때마다 1씩 소모, 한 승객을 목적지로 성공적으로 이동시키면 그 승객을 태워 이동하면서 소모한 연료 양의 두 배가 충전
# 이동 중 연료가 바닥나면 이동에 실패하고 그 날의 업무가 끝난다.
# 승객을 목적지로 이동시킨 동시에 연료가 바닥나는 경우는 실패한 것으로 간주하지 않는다.
# 모든 승객을 성공적으로 데려다줄 수 있다면 / 최종적으로 남는 연료의 양
# 실패하면 / -1

from collections import deque


N, M, gas = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
sy, sx = map(int, input().split())
sy, sx = sy-1, sx-1
guests = deque()
for _ in range(M):
    ay, ax, by, bx = map(int, input().split())
    guests.append((ay - 1, ax - 1, by - 1, bx - 1))
guests = sorted(guests)

for m in range(M):
    q = deque()
    visited = [[0] * N for _ in range(N)]
    q.append((sy, sx))
    visited[sy][sx] = 1

    while q:
        y, x = q.popleft()
        for (dy, dx) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0 and matrix[ny][nx] == 0:
                q.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1

    distance = []
    for (r, c, nr, nc) in guests:
        distance.append(visited[r][c])

    if max(distance) == 0:
        print(-1)
        break

    guest = guests[distance.index(min(distance))]

    gas = gas - visited[guest[0]][guest[1]] + 1

    if gas < 0:
        print(-1)
        break

    sy, sx = guest[0], guest[1]

    q = deque()
    visited = [[0] * N for _ in range(N)]
    q.append((guest[0], guest[1]))
    visited[sy][sx] = 1

    while q:
        y, x = q.popleft()
        for (dy, dx) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0 and matrix[ny][nx] == 0:
                q.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1

    if visited[guest[2]][guest[3]] == 0:
        print(-1)
        break

    gas = gas - visited[guest[2]][guest[3]] + 1

    guests.remove(guest)

    if gas < 0:
        print(-1)
        break

    gas = gas + (visited[guest[2]][guest[3]] - 1) * 2

    sy, sx = guest[2], guest[3]
else:
    print(gas)