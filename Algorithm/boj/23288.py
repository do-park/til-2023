# N * M, 오른쪽은 동쪽 위쪽은 북쪽
# (r, c): (1, 1) ~ (N, M)
# 주사위 각 면에는 1 ~ 6의 숫자
# 지도 위에 윗면이 1이고, 동쪽을 바라보는 방향이 3인 상태로 놓여져 있으며, 놓여진 좌표는 (1, 1)
# 가장 처음 주사위 이동 방향은 동족
# 주사위의 이동
# 1. 주사위가 이동 방향으로 한 칸 굴러간다. 만약 이동 방향에 칸이 없다면, 이동 방향을 반대로 한 다음 한 칸 굴러간다.
# 2. 주사위가 도착한 칸 (x, y)에 대한 점수를 획득한다.
# 3. 주사위의 아랫면에 있는 정수 A와 주사위가 있는 칸 (x, y)에 있는 정수 B를 비교해 이동 방향을 결정한다.
#       A > B 인 경우, 이동 방향을 90도 시계 방향으로 회전시킨다.
#       A < B 인 경우, 이동 방향을 90도 반시계 방향으로 회전시킨다.
#       A = B 인 경우, 이동 방향에 변화는 없다.
# 칸 (x, y)에 대한 점수는
# (x, y)에 있는 정수를 B라고 했을 때, (x, y)에서 동서남북 방향으로 연속해서 이동할 수 있는 칸의 수 C를 모두 구한다.
# 이때 이동할 수 있는 칸에는 모두 정수 B가 있어야 한다. 여기서 점수는 B와 C를 곱한 값이다.

# 보드의 크기와 각 칸에 있는 정수, 주사위의 이동 횟수 K가 주어졌을 때, 각 이동에서 획득하는 점수의 합을 구해보자.

from collections import deque


def rolling(DICE, D):
    if D == 0: # 동
        return [DICE[3], DICE[1], DICE[0], DICE[5], DICE[4], DICE[2]]
    elif D == 1: # 남
        return [DICE[1], DICE[5], DICE[2], DICE[3], DICE[0], DICE[4]]
    elif D == 2: # 서
        return [DICE[2], DICE[1], DICE[5], DICE[0], DICE[4], DICE[3]]
    else: # 북
        return [DICE[4], DICE[0], DICE[2], DICE[3], DICE[5], DICE[1]]


N, M, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
dist = [(0, 1), (1, 0), (0, -1), (-1, 0)]
y, x, d, score = 0, 0, 0, 0
dice = [1, 2, 3, 4, 5, 6]

for k in range(K):
    # 1
    ny, nx = y + dist[d][0], x + dist[d][1]
    if 0 <= ny < N and 0 <= nx < M:
        y, x = ny, nx

    else:
        d = (d + 2) % 4
        y, x = y + dist[d][0], x + dist[d][1]
    dice = rolling(dice, d)

    # 2
    B = matrix[y][x]
    q = deque()
    q.append((y, x))
    visited = [[0]*M for _ in range(N)]
    visited[y][x] = 1
    size = 1
    while q:
        (r, c) = q.popleft()
        for (dr, dc) in dist:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and matrix[nr][nc] == B:
                q.append((nr, nc))
                visited[nr][nc] = 1
                size += 1
    score += B * size

    # 3
    A = dice[-1]
    if A > B:
        d = (d + 1) % 4
    elif A < B:
        d = (3 + d) % 4

print(score)