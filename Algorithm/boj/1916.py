from heapq import heappush, heappop


INF = float('inf')
N = int(input())
M = int(input())
hq = []
routes = [[] for _ in range(N)]
result = [INF for _ in range(N)]
for _ in range(M):
    u, v, w = list(map(int, input().split()))
    routes[u-1].append((w, v-1))
start, end = map(int, input().split())
start, end = start-1, end-1

result[start] = 0
heappush(hq, [0, start])

while hq:
    cost, dist = heappop(hq)
    if result[dist] < cost:
        continue
    for (c, d) in routes[dist]:
        c += cost
        if result[d] > c:
            result[d] = c
            heappush(hq, (c, d))

print(result[end])