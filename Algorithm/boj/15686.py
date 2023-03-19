# N * N 도시, { 0: 빈 칸, 2: 치킨집, 1: 집 }, r행 c열
# 치킨 거리: 집과 가장 가까운 치킨집 사이의 거리
# 도시의 치킨 거리: 모든 치킨 거리의 합
# 거리는 |r1-r2| + |c1-c2|

# 폐업시키지 않을 치킨집 최대 M개 골랐을 때, 도시의 치킨 거리의 최솟값
from itertools import combinations


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
home, chicken = [], []
result = 987654321

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            home.append((i, j))
        elif matrix[i][j] == 2:
            chicken.append((i, j))

for c in combinations(chicken, M):
    city_chicken_distance = 0
    for h in home:
        home_chicken_distance = 987654321
        for m in range(M):
            home_chicken_distance = min(home_chicken_distance, abs(h[0] - c[m][0]) + abs(h[1] - c[m][1]))
        city_chicken_distance += home_chicken_distance
    result = min(result, city_chicken_distance)

print(result)
