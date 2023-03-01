N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]
y, x = N//2, N//2
cur = -1
count = 1
result = 0

# 아래(y) / 오른쪽(x)
drs = [[-1, -1, 0, 0, 2, 0, 0, 1, 1], [1, -1, 2, -2, 0, 1, -1, 1, -1]]
dcs = [[-1, 1, -2, 2, 0, -1, 1, -1, 1], [-1, -1, 0, 0, 2, 0, 0, 1, 1]]
rate = [1, 1, 2, 2, 5, 7, 7, 10, 10]


# axis 0: 세로 / 1 가로
def tornado(r, c, axis, curr):
    global result
    total_sand, left_sand = field[r][c], field[r][c]
    for s in range(9):
        nr, nc = r + drs[axis][s] * curr, c + dcs[axis][s] * curr
        sand = total_sand * rate[s] // 100
        if 0 <= nr < N and 0 <= nc < N:
            field[nr][nc] += sand
        else:
            result += sand
        left_sand -= sand
    # 남은 모래 전부 처리
    nr, nc = r + curr if axis == 0 else r, c + curr if axis == 1 else c
    if 0 <= nr < N and 0 <= nc < N:
        field[nr][nc] += left_sand
    else:
        result += left_sand


for i in range(1, N*2):
    for j in range(count):
        # 가로로 이동
        if i % 2 == 1:
            x = x + cur
            tornado(y, x, 1, cur)
        # 세로로 이동
        else:
            y = y + cur
            tornado(y, x, 0, cur)
        if (x, y) == (0, 0):
            break
    if i % 2 == 0:
        count += 1
    else:
        cur *= -1
print(result)