# 비바라기를 시전하면 하늘에 비구름을 만들 수 있다.
# N * N 격자. 각 칸에는 무제한 물바구니
# 격자의 가장 왼쪽 윗 칸 (1, 1), 오른쪽 아랫 칸은 (N, N)
# 1번 행과 N번 행은 연결 / 1번 열과 N번 열도 연결

# 비바라기를 시전하면 (N, 1), (N, 2), (N-1, 1), (N-2, 2)에 비구름이 생긴다.
# M번의 이동을 명령, i번째 이동 명령은 방향 d와 거리 s로 이루어져 있다.
# 8개의 방향이 있으며, 8개의 정수로 표현한다.


# 1. 모든 구름이 d 방향으로 s칸 이동
# 2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가
# 3. 구름이 모두 사라진다.
# 4. 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다. 물복사버그 마법을 사용하면, 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물의 양이 증가한다.
    # 이때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.
# 5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.

# M번이 이동이 끝난 후 바구니에 들어있는 물의 양의 합

dys = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dxs = [0, -1, -1, 0, 1, 1, 1, 0, -1]

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
spells = [list(map(int, input().split())) for _ in range(M)]
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

for [d, s] in spells:
    # 모든 구름이 d 방향으로 s칸 이동
    for i in range(len(clouds)):
        (y, x) = clouds[i]
        ny, nx = (N + y + dys[d] * s) % N, (N + x + dxs[d] * s) % N
        clouds[i] = (ny, nx)
        # 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가
        A[ny][nx] += 1

    # 물복사버그 마법
    for (y, x) in clouds:
        water = 0
        for (dy, dx) in [(-1, -1), (-1, 1), (1, 1), (1, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and A[ny][nx] > 0:
                water += 1
        A[y][x] += water

    # 새로운 구름이 생기고, 물의 양이 2 줄어든다
    temp = []
    for y in range(N):
        for x in range(N):
            if A[y][x] >= 2 and (y, x) not in clouds:
                temp.append((y, x))
                A[y][x] -= 2

    clouds = temp

result = 0
for a in A:
    result += sum(a)
print(result)