from heapq import heappop, heappush


N = int(input())
M = int(input())
routes = [[] for _ in range(N)]

for m in range(M):
    u, v, w = list(map(int, input().split()))
    routes[u-1].append((w, v-1))
    routes[v-1].append((w, u-1))

result = 0
visited = [False for _ in range(N)]
hq = []
visited[0] = True
for route in routes[0]:
    heappush(hq, route)


while hq:
    cost, dist = heappop(hq)
    if visited[dist]:
        continue
    result += cost
    visited[dist] = True
    for route in routes[dist]:
        heappush(hq, route)

print(result)