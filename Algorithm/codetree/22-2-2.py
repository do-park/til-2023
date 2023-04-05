from collections import deque


dists = [(-1, 0), (0, -1), (0, 1), (1, 0)]
N, M = map(int, input().split())
basecamp = [list(map(int, input().split())) for _ in range(N)]
stores = []
disabled = [[0] * N for _ in range(N)]
for _ in range(M):
    i, j = map(int, input().split())
    stores.append((i - 1, j - 1))
minute = 1
visited_list = [[[0] * N for _ in range(N)] for _ in range(M)]
q_list = [deque() for _ in range(M)]

while True:
    # 1
    # 격자에 있는 사람들이 본인이 가고 싶은 편의점 방향을 향해 1칸, 최단거리로 이동
    # 움직이는 방법이 여러가지라면 [ 위 왼쪽 오른쪽 아래 ] 의 우선순위로 움직임
    for idx in range(min(minute - 1, M)):
        if len(q_list[idx]) == 0:
            continue
        temp_q = deque()
        while q_list[idx]:
            (r, c) = q_list[idx].popleft()
            for (dr, dc) in dists:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and visited_list[idx][nr][nc] == 0 and disabled[nr][nc] == 0:
                    visited_list[idx][nr][nc] = visited_list[idx][r][c] + 1
                    temp_q.append((nr, nc))
        q_list[idx] = temp_q

    # 2
    # 편의점에 도착한다면 편의점에서 멈추고 다른 사람들은 해당 편의점이 있는 칸을 지나갈 수 없게 된다
    for idx in range(min(minute - 1, M)):
        if len(q_list[idx]) == 0:
            continue
        for (w, z) in q_list[idx]:
            if (w, z) == stores[idx]:
                q_list[idx] = deque()
                disabled[w][z] = 1
                break

    if minute >= M + 1 and q_list.count(deque()) == M:
        break

    # 3
    # 현재 시간이 t분이고 t<=m을 만족한다면 t번 사람은 자신이 가고 싶은 편의점과 가장 가까운 베이스캠프에 들어감
    # 최단거리 베이스캠프가 여러개인 경우 그 중 행이 작은 베이스캠프, 행이 같다면 열이 작은 베이스 캠프로 이동
    # 베이스캠프로 이동하는데는 시간이 들지 않고, 이때부터 다른 사람들은 해당 베이스캠프가 있는 칸을 지날 수 없음
    if minute <= M:
        distance = []
        visited = [[0]*N for _ in range(N)]
        q = deque()
        visited[stores[minute - 1][0]][stores[minute - 1][1]] = 1
        q.append((stores[minute - 1][0], stores[minute - 1][1]))

        while q:
            (y, x) = q.popleft()
            for (dy, dx) in dists:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0 and disabled[ny][nx] == 0:
                    if basecamp[ny][nx] == 1:
                        distance.append((visited[y][x] + 1, ny, nx))
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny, nx))

        distance.sort()
        basecamp[distance[0][1]][distance[0][2]] = 0
        disabled[distance[0][1]][distance[0][2]] = 1
        visited_list[minute-1][distance[0][1]][distance[0][2]] = 1
        q_list[minute-1].append((distance[0][1], distance[0][2]))

    minute += 1

print(minute)
