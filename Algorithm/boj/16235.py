from collections import deque


N, M, K = map(int, input().split())
land = [[5] * N for _ in range(N)]
s2d2 = [list(map(int, input().split())) for _ in range(N)]
trees = deque(list(map(int, input().split())) for _ in range(M))
dead_trees = deque()

for k in range(K):
    alive_trees = deque()
    baby_trees = deque()
    for tree in trees:
        [y, x, year] = tree
        if land[y-1][x-1] < year:
            dead_trees.append(tree)
        else:
            alive_trees.append([y, x, year + 1])
            land[y-1][x-1] -= year
    for tree in dead_trees:
        [y, x, year] = tree
        land[y-1][x-1] += year // 2
    for tree in alive_trees:
        [y, x, year] = tree
        if (year % 5) == 0:
            for (r, c) in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, +1), (1, -1), (1, 0), (1, 1)]:
                next_y, next_x = y + r, x + c
                if 0 <= next_y - 1 < N and 0 <= next_x -1 < N:
                    baby_trees.append([next_y, next_x, 1])
    for i in range(N):
        for j in range(N):
            land[i][j] += s2d2[i][j]
    trees = alive_trees
    trees.extend(baby_trees)


print(len(trees))