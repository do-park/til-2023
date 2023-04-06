# N * M 격자판, N번 행의 바로 아래(N+1행)의 모든 칸에는 성이 있다.
# 성이 있는 칸에 궁수 3명 배치, 하나의 칸에 한 명만 있을 수 있다.
# 각 턴마다 궁수는 적 하나를 공격, 모든 궁수는 동시에 공격한다.
# 궁수가 공격하는 적은 거리가 D이하인 적 중에서 가장 가까운 적
# 그러한 적이 여럿인 경우 왼쪽부터
# 같은 적이 여러 궁수에게 공격당할 수 있으며 공격받은 적은 게임에서 제외
# 궁수의 공격이 끝나면 적이 아래로 한 칸 이동
# 성이 있는 칸으로 이동한 경우에는 게임에서 제외된다. 모든 적이 격자 판에서 제외되면 게임에서 제외
# 모든 적이 격자판에서 제외되면 게임이 끝난다
# 격자판의 상태가 주어졌을 때 궁수의 공격으로 제거할 수 있는 적의 최대 수
import copy
from collections import deque

A = 3
N, M, D = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
answer = 0


def shooting(archer_pos, archer_map, idx, depth):
    global answer

    if depth == A:
        result = 0
        enemy = copy.deepcopy(matrix)
        for n in range(N):
            enemy.append(archer_map)
            height = len(enemy)
            shooted = [[0 for _ in range(M)] for _ in range(height)]
            killed = []
            for k in range(3):
                a_shooted = []
                q = deque()
                visited = [[0 for _ in range(M)] for _ in range(height)]
                q.append((height-1, archer_pos[k]))
                visited[height-1][archer_pos[k]] = 1

                while q:
                    (y, x) = q.popleft()
                    for (dy, dx) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < height-1 and 0 <= nx < M and not visited[ny][nx]:
                            if visited[y][x] <= D:
                                q.append((ny, nx))
                                visited[ny][nx] = visited[y][x] + 1
                                if enemy[ny][nx]:
                                    a_shooted.append((visited[y][x], nx, ny))  # ny, nx 아님!!!
                if len(a_shooted) > 0:
                    a_shooted.sort()
                    shooted[a_shooted[0][2]][a_shooted[0][1]] = 1
                    killed.append((a_shooted[0][2], a_shooted[0][1]))
            for s in shooted:
                result += s.count(1)
            for k in range(len(killed)):
                enemy[killed[k][0]][killed[k][1]] = 0
            enemy.pop()
            enemy.pop()
        answer = max(answer, result)
        return
    for m in range(idx, M):
        archer_pos.append(m)
        archer_map[m] = 1
        shooting(archer_pos, archer_map, m + 1, depth + 1)
        archer_pos.pop()
        archer_map[m] = 0


shooting([], [0 for _ in range(M)], 0, 0)
print(answer)