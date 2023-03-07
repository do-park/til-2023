# 마법사 상어와 복제
# 4 * 4 배열, (1, 1) ~ (4, 4)
# 물고기 M 마리, 각 물고기는 격자의 칸 하나에 들어가 있으며 이동 방향을 가지고 있다.
# 마법사 상어도 격자의 한 칸에 들어 있다.
# 둘 이상의 물고기가 같은 칸에 있을 수 있으며, 마법사 상어와 물고기도 같은 칸에 있을 수 있다.

# 1. 상어가 모든 물고기에게 복제 마법을 시전한다. 5에서 물고기가 복제되어 칸에 나타난다.
# 2. 모든 물고기가 한 칸 이동한다. 상어가 있는 칸, 물고기의 냄새가 있는 칸, 격자의 범위를 벗어나는 칸으로는 이동할 수 없다.
#    각 물고기는 자신이 가지고 있는 이동 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전시킨다.
#    만약 이동할 수 있는 칸이 없으면 이동을 하지 않는다. 그 외의 경우에는 그 칸으로 이동을 한다.
# 3. 상어가 연속해서 3칸 이동한다. 상어는 현재 칸에서 상하좌우로 인접한 칸으로 이동할 수 있다. 격자의 범위를 벗어날 수 없다.
#    이동하는 중에 상어가 물고기가 있는 같은 칸으로 이동하게 된다면, 그 칸에 있는 모든 물고기는 격자에서 제외되며
#    제외되는 모든 물고기는 물고기 냄새를 남긴다. 가능한 이동 방법 중에서 제외되는 물고기의 수가 가장 많은 방법으로 이동하며
#    그러한 방법이 여러가지인 경우 사전 순으로 가장 앞서는 방법을 이용한다.
# 4. 두 번 전 연습에서 생긴 물고기의 냄새가 격자에서 사라진다.
# 5. 1에서 사용한 복제 마법이 완료된다. 모든 복제된 물고기는 1에서의 위치와 방향을 그대로 갖게 된다.
from itertools import product

dys = [0, -1, -1, -1, 0, 1, 1, 1]
dxs = [-1, -1, 0, 1, 1, 1, 0, -1]

visited = [[0]*4 for _ in range(4)]
# 물고기의 수 M, 상어가 마법을 연습한 횟수 S
M, S = map(int, input().split())
# 물고기의 정보 (y, x, d) 위치 (y, x) 방향 d
# 상어 정보 (y, x)
fishes = []
for _ in range(M):
    y, x, d = map(int, input().split())
    fishes.append((y-1, x-1, d-1 if d > 0 else 7))
shark = list(map(int, input().split()))
shark[0], shark[1] = shark[0]-1, shark[1]-1

for s in range(S):
    matrix = [[[] * 4 for _ in range(4)] for __ in range(4)]
    # 1
    new_fishes = fishes
    # 2
    for fish in fishes:
        (y, x, d) = fish
        for n in range(8):
            nd = (d-n) % 8
            ny, nx = y + dys[nd], x + dxs[nd]
            if 0 <= ny < 4 and 0 <= nx < 4 and not visited[ny][nx] and [ny, nx] != shark:
                matrix[ny][nx].append(nd)
                break
        else:
            matrix[y][x].append(d)

    # 3
    shark_d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    largest_pp = (-1, -1, -1)
    largest_total = 0
    for pp in product([0, 1, 2, 3], repeat=3):
        temp = matrix
        ny, nx = shark[0], shark[1]
        total = 0
        for p in pp:
            dy, dx = shark_d[p]
            ny, nx = ny + dy, nx + dx
            if 0 <= ny < 4 and 0 <= nx < 4:
                total += len(temp[ny][nx])
                temp[ny][nx] = []
            else:
                break
        else:
            if largest_total < total:
                largest_total = total
                largest_pp = pp

    ny, nx = shark[0], shark[1]
    for p in largest_pp:
        dy, dx = shark_d[p]
        ny, nx = ny + dy, nx + dx




    # 4
    for y in range(4):
        for x in range(4):
            if matrix[y][x]:
                for fish in matrix[y][x]:
                    new_fishes.append((y, x, fish))
    fish = new_fishes

