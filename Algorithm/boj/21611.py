# 마법사 상어와 블리자드
# N * N 격자 (N은 홀수)
# 격자는 1, 1 ~ N, N까지
# 마법사 상어는 ((N+1)/2, (N+1)/2)


ds = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
start = (N + 1)//2 - 1
result = 0

for m in range(M):
    [d, s] = list(map(int, input().split()))
    y, x = start, start
    # d 방향으로 거리 s 이하인 모든 칸에 얼음 파편을 던져 그 칸에 있는 구슬을 모두 파괴한다.
    for i in range(s):
        y, x = y + ds[d][0], x + ds[d][1]
        matrix[y][x] = 0
    # 어떤 칸 A의 번호보다 번호가 하나 작은 칸이 빈 칸이면, A에 있는 구슬은 그 빈 칸으로 이동한다.
    balls = []
    y, x, cur = start, start, -1
    for n in range(N):
        # 왼쪽으로 n번
        for i in range(n + 1):
            x += cur
            if x < 0:
                break
            balls.append(matrix[y][x])
        if x < 0:
            break
        cur *= -1
        # 아래쪽으로 n번
        for i in range(n + 1):
            y += cur
            balls.append(matrix[y][x])

    balls = [ball for ball in balls if ball != 0]
    # 더 이상 폭발하는 구슬이 없을 때까지
    # 4개 이상 연속하는 구슬이 있을 때 구슬은 폭발한다. (이 때 폭발하는 구슬의 수 구해야 함)
    # 어떤 칸 A의 번호보다 번호가 하나 작은 칸이 빈 칸이면, A에 있는 구슬은 그 빈 칸으로 이동한다.
    while True:
        start_len = len(balls)
        count = 0
        for i in range(1, len(balls)):
            if balls[i] == balls[i - 1]:
                count += 1
            else:
                if count >= 3:
                    for c in range(1, count + 2):
                        result += balls[i - c]
                        balls[i - c] = 0
                count = 0
        if count >= 3:
            for c in range(1, count + 2):
                result += balls[-c]
                balls[-c] = 0

        balls = [ball for ball in balls if ball != 0]
        end_len = len(balls)

        if start_len == end_len:
            break

    if len(balls) == 0:
        break
    # 연속한 구슬을 하나의 그룹이라고 하고 (구슬의 개수, 구슬의 번호) 로 치환되어 빈 칸에 들어간다.
    new_balls = []
    count = 1
    for i in range(1, len(balls)):
        if balls[i] == balls[i - 1]:
            count += 1
        else:
            new_balls.append(count)
            new_balls.append(balls[i - 1])
            count = 1
    new_balls.append(count)
    new_balls.append(balls[-1])

    y, x, cur, idx, length = start, start, -1, 0, len(new_balls)
    for n in range(N):
        # 왼쪽으로 n번
        for i in range(n + 1):
            x += cur
            if x < 0:
                break
            matrix[y][x] = new_balls[idx] if length > idx else 0
            idx += 1
        if x < 0:
            break
        cur *= -1
        # 아래쪽으로 n번
        for i in range(n + 1):
            y += cur
            matrix[y][x] = new_balls[idx] if length > idx else 0
            idx += 1
print(result)