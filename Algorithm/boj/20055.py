# 길이가 N인 컨베이어 벨트, 길이가 2N인 벨트가 컨베이어 벨트를 감싸며 돌고 있다.
# 1번 칸이 있는 위치를 올리는 위치, N번칸이 있는 위치를 내리는 위치
# 컨베이어 벨트에 박스 모양 로봇을 하나씩 올린다.
# 올리는 위치에만 올릴 수 있고, 내리는 위치에 도달하면 즉시 내린다.
# 로봇은 컨베이어 벨트에서 스스로 이동할 수 있다.
# 로봇을 올리는 위치에 올리거나 로봇이 어떤 칸으로 이동하면 그 칸의 내구도는 즉시 1만큼 감소한다.

# 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 이동
# 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동
#    로봇이 이동하려면 이동하려는 칸에 로봇이 없어야 하며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
# 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
# 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.

# 종료되었을 때 몇 번째 단계가 진행 중이었는지 구해보자. 처음 수행되는 단계는 1번째 단계이다.

from collections import deque


N, K = map(int, input().split())
belt = deque(list(map(int, input().split())))
robots = deque([False] * N)
result = 0

while True:
    result += 1
    # 1
    belt.rotate(1)
    robots.rotate(1)

    if robots[N-1]:
        robots[N-1] = False

    # 2
    for n in range(N-1, 0, -1):
        if belt[n] > 0 and not robots[n] and robots[n-1]:
            robots[n], robots[n-1] = True, False
            belt[n] -= 1

    if robots[N-1]:
        robots[N-1] = False

    # 3
    if belt[0] > 0:
        robots[0] = True
        belt[0] -= 1

    if belt.count(0) >= K:
        break

print(result)