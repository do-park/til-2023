# 2^N * 2^N 격자로 나누어진 얼음판
# A[r][c]=0 격자 r행 c열의 얼음 양은 0
# 단계 L
# 격자를 2^L * 2^L 크기의 부분 격자로 나누고 모든 부분 격자를 시계 방향으로 90도 회전
# 이후 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다.
# 인접한 칸은 상하좌우
# 파이어스톰 총 Q번 시행, 시행 후 [남아있는 얼음 A[r][c]의 합 / 남아있는 얼음 중 가장 큰 덩어리를 차지하는 칸의 개수]

from collections import deque

dists = [(-1, 0), (0, 1), (1, 0), (0, -1)]

N, Q = map(int, input().split())
size = pow(2, N)
field = [list(map(int, input().split())) for _ in range(size)]
spells = list(map(int, input().split()))

for spell in spells:
    # 격자를 나눠서 시계 방향으로 회전
    l_size = pow(2, spell)
    for i in range(0, size, l_size):
        for j in range(0, size, l_size):
            temp = [[0]*l_size for _ in range(l_size)]
            for y in range(l_size):
                for x in range(l_size):
                    temp[y][x] = field[i + l_size-1-x][j + y]

            for y in range(l_size):
                for x in range(l_size):
                    field[i + y][j + x] = temp[y][x]
    # 얼음 3칸 이상 접하지 않은 곳 1씩 녹음
    temp = [[0]*size for _ in range(size)]
    for y in range(size):
        for x in range(size):
            if field[y][x]:
                count = 0
                for (dy, dx) in dists:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < size and 0 <= nx < size and field[ny][nx] > 0:
                        count += 1
                temp[y][x] = field[y][x] if count >= 3 else field[y][x] - 1
    field = temp

left_ice = 0
biggest_ice = 0

for row in field:
    for ice in row:
        left_ice += ice
print(left_ice)

Q = deque()
visited = [[0]*size for _ in range(size)]
for i in range(size):
    for j in range(size):
        if not visited[i][j] and field[i][j] > 0:
            visited[i][j] = 1
            Q.append((i, j))
            size_of_ice = 1
            while Q:
                (y, x) = Q.popleft()
                for (dy, dx) in dists:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < size and 0 <= nx < size and not visited[ny][nx] and field[ny][nx]:
                        visited[ny][nx] = 1
                        Q.append((ny, nx))
                        size_of_ice += 1
            biggest_ice = biggest_ice if biggest_ice > size_of_ice else size_of_ice
print(biggest_ice)