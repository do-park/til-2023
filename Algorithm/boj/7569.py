# 가로 M 세로 N 높이 H
# 보관 후 하루가 지나면 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익는다.
# 인접한 곳: 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
# 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지
# 일부 칸에는 토마토가 들어있지 않을 수도 있다.

# M, N, H
# 1 익은 토마토, 0 안 익은 토마토, -1 빈 칸

from collections import deque


dzs = [-1, 1, 0, 0, 0, 0]
dys = [0, 0, -1, 1, 0, 0]
dxs = [0, 0, 0, 0, -1, 1]

M, N, H = map(int, input().split())
tomatoes = [[list(map(int, input().split())) for _ in range(N)] for __ in range(H)]

ripen_tomatoes = deque()

# 토마토 순회하면서 익은 토마토 골라냄(좌표 ripen에 넣기) + 전체 토마토의 개수 카운트
# ripen 토마토 bfs 돌리기 / 전체 토마토 개수에서 익은 토마토 개수 빼주기
# ripen 토마토 비었을 때, 전체 토마토 개수가 0이 되었으면 bfs 돈 횟수 리턴 / 아니면 -1 리턴

last_tomatoes = 0

for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomatoes[h][n][m] == 1:
                ripen_tomatoes.append([h, n, m])
            elif tomatoes[h][n][m] == 0:
                last_tomatoes += 1

result = 0

while ripen_tomatoes and last_tomatoes > 0:
    temp = deque()
    while ripen_tomatoes:
        [h, n, m] = ripen_tomatoes.popleft()
        for (dz, dy, dx) in zip(dzs, dys, dxs):
            next_h, next_n, next_m = h + dz, n + dy, m + dx
            if 0 <= next_h < H and 0 <= next_n < N and 0 <= next_m < M and tomatoes[next_h][next_n][next_m] == 0:
                temp.append([next_h, next_n, next_m])
                tomatoes[next_h][next_n][next_m] = 1
                last_tomatoes -= 1
    result += 1
    ripen_tomatoes = temp

print(-1 if last_tomatoes > 0 else result)