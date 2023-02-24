N, M, K = map(int, input().split())
soil = [[5] * N for _ in range(N)]
s2d2 = [list(map(int, input().split())) for _ in range(N)]

trees = [[[] for _ in range(N)] for __ in range(N)]
for _ in range(M):
    r, c, year = map(int, input().split())
    trees[r - 1][c - 1].append(year)

for k in range(K):
    next_generation = [[[] for _ in range(N)] for __ in range(N)]
    for r in range(N):
        for c in range(N):
            trees[r][c].sort()
            nutrition = 0
            for tree in trees[r][c]:
                if tree <= soil[r][c]:
                    soil[r][c] -= tree
                    tree += 1
                    next_generation[r][c].append(tree)
                    if tree % 5 == 0:
                        for (y, x) in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, +1), (1, -1), (1, 0), (1, 1)]:
                            next_r, next_c = y + r, x + c
                            if 0 <= next_r < N and 0 <= next_c < N:
                                next_generation[next_r][next_c].append(1)
                else:
                    nutrition += tree // 2
            soil[r][c] += nutrition
            soil[r][c] += s2d2[r][c]
    trees = next_generation

answer = 0

for r in range(N):
    for c in range(N):
        answer += len(trees[r][c])
print(answer)