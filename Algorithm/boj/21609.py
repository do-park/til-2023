# 상어 중학교

# N * N 격자
# 초기 격자의 모든 칸에는 블록이 하나씩
# 검은색(-1) / 무지개(0) / 일반 (M가지 색상)
# 인접한 칸: 상하좌우

# 1. 크기가 가장 큰 블록 그룹
# 1-1. 블록 그룹이 여러 개라면 포함된 무지개 블록의 수가 가장 많은 블록 그룹
#      그런 블록도 여러개라면 기준 블록의 행이 가장 큰 것을, 그것도 여러개이면 열이 가장 큰 것
# 2. 1에서 찾은 블록 그룹의 모든 블록을 제거. 블록 그룹에 포함된 블록의 수를 B라고 했을 때 b^2점을 획득
# 3. 격자에 중력이 작용
# 4. 격자가 90도 반시계 방향으로 회전한다.
# 5. 다시 격자에 중력이 작용한다.

# 격자에 중력이 작용하면 검은색 블록을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동한다.
# 이동은 다른 블록이나 격자의 경계를 만나기 전까지 계속 된다.

# 오토 플레이가 끝났을 때 획득한 점수의 합
# 오토플레이는 블록 그룹이 존재하는 동안 계속 반복되어야 한다.

# 격자 한 변의 크기 N, 색상의 개수 M
# 둘째 줄부터 N개의 줄에 격자의 칸에 들어가 있는 블록의 정보가 1번 행부터 N번 행까지 순서대로

from collections import deque

dists = [(-1, 0), (0, 1), (1, 0), (0, -1)]

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
score = 0

while True:
    # 1. 블록 그룹 찾기
    visited = [[0]*N for _ in range(N)]
    block_group = []
    block_group_size, block_group_rainbow = 0, 0
    for r in range(N):
        for c in range(N):
            if 0 < matrix[r][c] != visited[r][c]:
                group = []
                group_size, rainbow = 1, 0
                q = deque()
                q.append((r, c))
                visited[r][c] = matrix[r][c]
                group.append((r, c))
                while q:
                    (y, x) = q.popleft()
                    for (dy, dx) in dists:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] != matrix[r][c]:
                            if matrix[ny][nx] == matrix[r][c]:
                                group.append((ny, nx))
                                q.append((ny, nx))
                                visited[ny][nx] = matrix[r][c]
                                group_size += 1
                            elif matrix[ny][nx] == 0:
                                group.append((ny, nx))
                                q.append((ny, nx))
                                visited[ny][nx] = matrix[r][c]
                                group_size += 1
                                rainbow += 1
                if block_group_size < group_size:
                    block_group, block_group_size, block_group_rainbow = group, group_size, rainbow
                elif block_group_size == group_size and block_group_rainbow <= rainbow:
                    block_group, block_group_size, block_group_rainbow = group, group_size, rainbow

    if block_group_size <= 1:
        break

    # 2. 블록 그룹 제거, 블록 그룹 제곱 점수 획득
    for (r, c) in block_group:
        matrix[r][c] = -2

    score += pow(block_group_size, 2)

    # 3. 격자에 중력이 작용, 검은색 블록을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동
    for r in range(N-1, -1, -1):
        for c in range(N):
            if matrix[r][c] == -2:
                for i in range(1, r + 1):
                    j = r - i
                    if matrix[r - i][c] == -1:
                        break
                    if matrix[r - i][c] >= 0:
                        matrix[r][c], matrix[r - i][c] = matrix[r - i][c], -2
                        break

    # 4. 격자가 90도 반시계 방향으로 회전
    temp = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            temp[r][c] = matrix[c][N - 1 - r]

    # 5.다시 격자에 중력이 작용, 검은 블록을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동
    for r in range(N-1, -1, -1):
        for c in range(N):
            if temp[r][c] == -2:
                for i in range(1, r + 1):
                    j = r - i
                    if temp[r - i][c] == -1:
                        break
                    if temp[r - i][c] >= 0:
                        temp[r][c], temp[r - i][c] = temp[r - i][c], -2
                        break

    matrix = temp

print(score)