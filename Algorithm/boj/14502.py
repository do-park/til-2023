import copy
from collections import deque


N, M = map(int, input().split())
matrix = []
space, virus = [], []

for n in range(N):
    temp = list(map(int, input().split()))
    for m in range(M):
        if temp[m] == 2:
            virus.append((n, m))
        elif temp[m] == 0:
            space.append((n, m))
    matrix.append(temp)

# 모든 빈칸(0)에는 벽을 세울 수 있다.
# 벽(1)으로는 바이러스(2)가 퍼질 수 없다.

result = -1
q = deque()
len_of_space = len(space)
default_safe_area = len_of_space - 3


def solution(start, depth):
    global result, q

    if depth == 3:
        safe_area = default_safe_area
        new_matrix = copy.deepcopy(matrix)
        new_q = copy.deepcopy(q)
        visited = [[0 for __ in range(M)] for _ in range(N)]
        for v in virus:
            new_q.append(v)
            visited[v[0]][v[1]] = 1

        while new_q:
            (y, x) = new_q.popleft()
            for (dy, dx) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < M and new_matrix[ny][nx] == 0 and not visited[ny][nx]:
                    new_q.append((ny, nx))
                    visited[ny][nx] = 1
                    safe_area -= 1

        result = max(result, safe_area)
        return

    for i in range(start, len_of_space):
        y, x = space[i]
        matrix[y][x] = 1
        solution(i + 1, depth + 1)
        matrix[y][x] = 0


solution(0, 0)
print(result)