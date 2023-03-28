# 집 N개, 집의 좌표 x1 ~ xn, 집 여러개가 같은 좌표를 가지는 일은 없다.
# 집에 공유기 C개 설치
# 한 집에는 공유기를 하나만, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치
# C개의 공유기를 N개의 집에 적당히 설치, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램

N, C = map(int, input().split())
C -= 1
houses = [int(input()) for _ in range(N)]
houses.sort()
st, en = 0, houses[N - 1]
result = 0

while st <= en:
    mid = (st + en) // 2
    cnt = 0
    setted = houses[0]
    for n in range(1, N):
        diff = houses[n] - setted
        if diff >= mid:
            cnt += 1
            setted = houses[n]

    if cnt < C:
        en = mid - 1
    else:
        st = mid + 1
        result = mid

print(result)
