# N * N 격자에 파이어볼 M개
# 파이어볼 무빙
# 1. 처음에 각자 위치에서 이동 대기
#    i 번째 파이어볼의 위치는 (r, c), 질량 m 방향 d 속력 s
#    격자의 행과 열은 1~N까지, 1번 행은 N번 행과, 1번 열은 N번 열과 연결
#    파이어볼의 방향은 어떤 칸과 인접한 8개의 칸의 방향

# 2. 상어가 파이어볼에게 이동을 명령하면
#    모든 파이어볼의 자신의 방향 d로 속력 s칸 만큼 이동한다.
#         이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.
#    이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
#         1. 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
#         2. 파이어볼은 4개의 파이어볼로 나누어진다.
#         3. 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
#            질량은 합쳐진 파이어볼의 질량의 합 // 5
#            속력은 합쳐진 파이어볼의 속력의 합 // 합쳐진 파이어볼의 개수
#            합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면 방향은 0, 2, 4, 6 / 아니면 1, 3, 5, 7
#         4. 질량이 0인 파이어볼은 소멸되어 없어진다.

# RESULT 마법사 상어가 이동을 k번 명령한 후, 남아있는 파이어볼의 질량의 합

dys = [-1, -1, 0, 1, 1, 1, 0, -1]
dxs = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
fields = [[[] * N for _ in range(N)] for __ in range(N)]
for fireball in range(M):
    r, c, m, s, d = map(int, input().split())
    fields[r-1][c-1].append([m, s, d])

for k in range(K):
    temp = [[[]*N for _ in range(N)] for __ in range(N)]
    for y in range(N):
        for x in range(N):
            for ball in fields[y][x]:
                m, s, d = ball
                ny, nx = (y + dys[d]*s + N) % N, (x + dxs[d]*s + N) % N
                temp[ny][nx].append([m, s, d])

    for y in range(N):
        for x in range(N):
            if len(temp[y][x]) > 1:
                count = len(temp[y][x])
                sum_m, sum_s = 0, 0
                is_every_d_even = 0
                for [m, s, d] in temp[y][x]:
                    sum_m += m
                    sum_s += s
                    is_every_d_even = is_every_d_even + 1 if d % 2 == 0 else is_every_d_even

                new_field = []
                nm, ns = sum_m // 5, sum_s // count
                if nm > 0:
                    if is_every_d_even == 0 or is_every_d_even == count:
                        for nd in [0, 2, 4, 6]:
                            new_field.append([nm, ns, nd])
                    else:
                        for nd in [1, 3, 5, 7]:
                            new_field.append([nm, ns, nd])
                temp[y][x] = new_field

    fields = temp

result = 0
for field in fields:
    for fireballs in field:
        for ball in fireballs:
            result += ball[0]

print(result)