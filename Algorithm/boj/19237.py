# 상어 1 ~ M 자연수 번호, 모든 번호는 다르다
# N * N 격자 중 M개의 칸에 상어가 한 마리
# 모든 상어가 자신의 위치에 자신의 냄새를 뿌리고, 상하좌우로 인접한 칸 중 하나로 이동해 자신의 냄새를 뿌린다.
# 냄새는 k번 이동하고 나면 사라진다.
# 이동 방향은 인접한 칸 중 아무 냄새가 없는 칸부터, 그런 칸이 없으면 자신의 냄새가 있는 칸으로
# 같은 조건인 경우 특정 우선순위에 따라 다르다.
# 모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면 가장 작은 번호의 상어만 남는다.
# 1번 상어만 남을 때 까지 몇 초가 걸리는지, 1000초가 넘으면 -1

N, M, K = map(int, input().split())
sharks = [(-1, -1) for _ in range(M + 1)]
visited = [[(0, 0) for _ in range(N)] for _ in range(N)] # shark idx, smells
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] != 0:
            sharks[temp[j]] = (i, j)
            visited[i][j] = (temp[j], K)
# 0 위 1 왼쪽 2 아래 3 오른쪽
dists = [(-1, 0), (1, 0), (0, -1), (0, 1)]
sharks_d = [0] + list(map(int, input().split()))
for m in range(M+1):
    sharks_d[m] -= 1
moves = [[]]
for m in range(M):
    temps = []
    for i in range(4):
        temp = list(map(int, input().split()))
        for j in range(4):
            temp[j] -= 1
        temps.append(temp)
    moves.append(temps)

result = -1
for second in range(1, 1001):
    next_moves = [[[] for _ in range(N)] for _ in range(N)]
    for idx in range(1, M + 1):
        (y, x) = sharks[idx]

        if (y, x) == (-1, -1):
            continue

        shark_move = moves[idx][sharks_d[idx]]
        for d in range(4):
            (dy, dx) = dists[shark_move[d]]
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == (0, 0):
                next_moves[ny][nx].append(idx)
                sharks_d[idx] = shark_move[d]
                break
        else:
            for d in range(4):
                (dy, dx) = dists[shark_move[d]]
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < N and (visited[ny][nx][0] == idx):
                    next_moves[ny][nx].append(idx)
                    sharks_d[idx] = shark_move[d]
                    break

    for i in range(N):
        for j in range(N):
            if visited[i][j] == (0, 0):
                continue
            elif visited[i][j][1] == 1:
                visited[i][j] = (0, 0)
            elif visited[i][j][1] > 1:
                visited[i][j] = (visited[i][j][0], visited[i][j][1] - 1)

    for r in range(N):
        for c in range(N):
            if len(next_moves[r][c]) == 0:
                continue
            elif len(next_moves[r][c]) == 1:
                index = next_moves[r][c][0]
                visited[r][c] = (index, K)
                sharks[index] = (r, c)
            elif len(next_moves[r][c]) > 1:
                index = min(next_moves[r][c])
                visited[r][c] = (index, K)
                sharks[index] = (r, c)
                for i in range(len(next_moves[r][c])):
                    if next_moves[r][c][i] != index:
                        sharks[next_moves[r][c][i]] = (-1, -1)

    if M + 1 - sharks.count((-1, -1)) == 1:
        result = second
        break

print(result)
