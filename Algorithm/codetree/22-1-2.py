# 초기 예술 점수 + 1회전 이후 예술 점수 + 2회전 이후 예술 점수 + 3회전 이후 예술 점수

# 동일한 숫자가 상하좌우로 인접해있는 경우 동일한 그룹이라 본다
# 예술 점수는 모든 그룹 쌍의 조화로움의 합
# 조화로움은 (그룹 a에 속한 칸의 수 + 그룹 b에 속한 칸의 수) * 그룹 a를 이루고 있는 숫자 값 * 그룹 b를 이루고 있는 숫자 값 * 그룹 a와 b가 맞닿아 있던 변의 수
# 그룹쌍 간의 조화로움값을 모두 더한 것을 초기 예술 점수

# 그림에 대한 화전
# 십자 모양과 그 외 부분
# 십자 모양은 통째로 반시계 방향으로 90도 회전
# 나머지 4개의 정사각형은 개별적으로 시계방향으로 90도씩 회전
# 새로운 그림에 대한 예술 점수를 같은 방법으로 계산
from collections import deque


dists = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
half_N = N // 2


def calc_score(picture):
    # 그룹 만들기 (0부터 시작, group_number개의 그룹 생성)
    group_number = 0
    group_picture = [[-1 for __ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if group_picture[r][c] == -1:
                q = deque()
                q.append((r, c))
                group_picture[r][c] = group_number
                while q:
                    (y, x) = q.popleft()
                    for (dy, dx) in dists:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < N and 0 <= nx < N and picture[r][c] == picture[ny][nx] and group_picture[ny][nx] == -1:
                            q.append((ny, nx))
                            group_picture[ny][nx] = group_number
                group_number += 1

    # 조화로움 계산
    score = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    # 그룹 a의 칸의 수, 그룹 a의 숫자 값, 다른 그룹과 맞닿아 있는 변의 수
    COUNT, VALUE, EDGE = 0, 1, 2
    group_info = [[0, 0, [0 for __ in range(group_number)]] for _ in range(group_number)]
    for r in range(N):
        for c in range(N):
            if visited[r][c] == 0:
                number = group_picture[r][c]
                group_info[number][VALUE] = picture[r][c]
                q = deque()
                q.append((r, c))
                visited[r][c] = 1
                group_info[number][COUNT] += 1
                while q:
                    (y, x) = q.popleft()
                    for (dy, dx) in dists:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0:
                            if group_picture[ny][nx] == number:
                                q.append((ny, nx))
                                visited[ny][nx] = 1
                                group_info[number][COUNT] += 1
                            else:
                                group_info[number][EDGE][group_picture[ny][nx]] += 1
                                group_info[group_picture[ny][nx]][EDGE][number] += 1

    for r in range(group_number):
        for c in range(r + 1, group_number):
            g1, g2 = group_info[r], group_info[c]
            if g1[EDGE][c] == 0:
                continue
            score += (g1[COUNT] + g2[COUNT]) * g1[VALUE] * g2[VALUE] * g1[EDGE][c]

    # 예술 점수 반환
    return score


def rotate_picture(picture):
    rotated = [[0 for _ in range(N)] for _ in range(N)]

    # 십자 모양 회전
    for r in range(N):
        rotated[half_N][r], rotated[r][half_N] = picture[r][half_N], picture[half_N][N - r - 1]
    # 나머지 부분 회전
    for r in range(half_N):
        for c in range(half_N):
            rotated[r][c] = picture[half_N - c - 1][r]
            rotated[half_N + 1 + r][c] = picture[N - c - 1][r]
            rotated[r][half_N + c + 1] = picture[half_N - 1 - c][half_N + 1 + r]
            rotated[half_N + 1 + r][half_N + c + 1] = picture[N - 1 - c][half_N + r + 1]

    # 회전된 그림 반환
    return rotated


result = 0
for i in range(4):
    result += calc_score(matrix)
    matrix = rotate_picture(matrix)
print(result)