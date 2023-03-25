import heapq


INF = float('inf')
V, E = map(int, input().split())
K = int(input()) - 1
matrix = [[] for _ in range(V)]
result = [INF]*V
result[K] = 0
hq = [(0, K)]

for e in range(E):
    iu, iv, iw = map(int, input().split())
    iu, iv = iu-1, iv-1
    matrix[iu].append((iv, iw))

while hq:
    dist, vertex = heapq.heappop(hq)
    if dist > result[vertex]:
        continue
    edges = matrix[vertex]
    for (v, w) in edges:
        next_dist = dist + w
        if result[v] > next_dist:
            result[v] = next_dist
            heapq.heappush(hq, (next_dist, v))

for r in result:
    print('INF' if r == INF else r)