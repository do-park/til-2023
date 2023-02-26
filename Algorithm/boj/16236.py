# N * N 공간에 물고기 M마리와 아기상어 1마리
# 한 칸에는 최대 물고기 1마리가 존재
# 아기 상어와 물고기 모두 크기를 가지고 있고, 이 크기는 자연 수
# 아기 상어 초기 크기 2, 1초에 상하좌우로 인접한 한 칸씩 이동
# 자기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 지나갈 수 있다.
# 자신보다 작은 물고기만 먹을 수 있고, 크기가 같은 물고기가 있는 칸은 지나갈 수만 있다.

# 아기 상어의 이동
# 더 먹을 수 있는 물고기가 공간에 없으면 엄마 상어에게 도움을 요청
# 먹을 수 있는 물고기가 1마리면 그 물고기를 먹으러 간다.
# 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
    # 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야 하는 칸의 개수의 최솟값
    # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그런 물고기가 여러마리라면 가장 왼쪽에 있는 물고기
# 이동에는 1초가 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정. 먹고 나면 그 칸은 빈칸이 된다.

# 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때마다 크기가 1 증가한다.

# SOLVE : 공간의 상태가 주어졌을 때, 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지

from collections import deque


Q = deque()
dys = [-1, 0, 0, 1]
dxs = [0, -1, 1, 0]


N = int(input())
ocean = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
size_of_shark = 2
exp = 0
answer = 0

for j in range(N):
    for i in range(N):
        if ocean[j][i] == 9:
            Q.append((0, j, i))
            visited[j][i] = 1
            ocean[j][i] = 0

while Q:
    (dist, y, x) = Q.popleft()
    if 0 < ocean[y][x] < size_of_shark:
        answer += dist
        ocean[y][x] = 0
        dist = 0
        Q = deque()
        visited = [[0] * N for _ in range(N)]
        visited[y][x] = 1
        exp += 1
        if size_of_shark == exp:
            size_of_shark += 1
            exp = 0

    for (dy, dx) in zip(dys, dxs):
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0:
            if 0 <= ocean[ny][nx] <= size_of_shark:
                Q.append((dist + 1, ny, nx))
            visited[ny][nx] = 1
    Q = deque(sorted(Q))

print(answer)