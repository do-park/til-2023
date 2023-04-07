Y, X, D, S, G = 0, 1, 2, 3, 4
dists = [(-1, 0), (0, 1), (1, 0), (0, -1)]

N, M, K = map(int, input().split())
matrix = [[[] for _ in range(N)] for __ in range(N)]

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        matrix[i][j].append(temp[j])

pos = [[-1] * N for __ in range(N)]
players = []
for i in range(M):
    o, p, q, r = map(int, input().split())
    players.append([o-1, p-1, q, r, 0])
    pos[o-1][p-1] = i

result = [0 for _ in range(M)]
for k in range(K):
    for idx in range(M):
        # 1-1
        y, x = players[idx][Y], players[idx][X]
        ny, nx = 0, 0
        for d in range(0, 4, 2):
            nd = (players[idx][D] + d) % 4
            y, x = players[idx][Y], players[idx][X]
            ny, nx = players[idx][Y] + dists[nd][Y], players[idx][X] + dists[nd][X]
            if 0 <= ny < N and 0 <= nx < N:
                players[idx][D] = nd
                break

        # 2-1
        if pos[ny][nx] == -1:
            if max(matrix[ny][nx]) > players[idx][G]:
                players[idx][G], matrix[ny][nx][matrix[ny][nx].index(max(matrix[ny][nx]))]\
                    = max(matrix[ny][nx]), players[idx][G]
            pos[ny][nx], pos[players[idx][Y]][players[idx][X]] = idx, -1
            players[idx][Y], players[idx][X] = ny, nx
        else:
            # 2-2-1 / 2-2-2
            another_idx = pos[ny][nx]
            a, b = players[idx][S] + players[idx][G], players[another_idx][S] + players[another_idx][G]
            winner, loser = another_idx, idx
            if a > b:
                winner, loser = idx, another_idx
            elif a == b:
                if players[idx][S] > players[another_idx][S]:
                    winner, loser = idx, another_idx

            result[winner] += players[winner][S] + players[winner][G] - players[loser][S] - players[loser][G]
            matrix[ny][nx].append(players[loser][G])
            players[loser][G] = 0
            for d in range(4):
                nd = (players[loser][D] + d) % 4
                nny, nnx = ny + dists[nd][Y], nx + dists[nd][X]
                if 0 <= nny < N and 0 <= nnx < N and (pos[nny][nnx] == -1 or pos[nny][nnx] == idx):
                    if pos[nny][nnx] == -1:
                        pos[y][x] = -1
                    players[loser][D] = nd
                    pos[nny][nnx] = loser
                    players[loser][Y], players[loser][X] = nny, nnx
                    if max(matrix[nny][nnx]) > players[loser][G]:
                        players[loser][G] = max(matrix[nny][nnx])
                        matrix[nny][nnx][matrix[nny][nnx].index(max(matrix[nny][nnx]))] = 0
                    break

            pos[ny][nx] = winner
            players[winner][Y], players[winner][X] = ny, nx
            if max(matrix[ny][nx]) > players[winner][G]:
                players[winner][G], matrix[ny][nx][matrix[ny][nx].index(max(matrix[ny][nx]))]\
                    = max(matrix[ny][nx]), players[winner][G]

print(*result)
