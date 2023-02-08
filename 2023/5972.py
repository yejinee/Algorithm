import heapq
import sys
input = sys.stdin.readline
INF = 1e9

def solution(road_info, start, end):
    q = []  # 우선순위큐
    heapq.heappush(q, (0, start))

    distance = [INF] * (n+1)
    distance[start] = 0


    while q:
        cost, node = heapq.heappop(q)
        if node == n:
            return distance[node]
        # if distance[node] < cost:
        #     continue

        # next와 연결된 곳 구하기
        for ncost, nnode in road_info[node]:
            if ncost + cost < distance[nnode]:
                distance[nnode] = ncost + cost
                heapq.heappush(q, (cost + ncost, nnode))


n, m = map(int, input().split())
road_info = [[] for _ in range(n+1)]
for i in range(m):
    a, b, cost = map(int, input().split())
    road_info[a].append((cost, b))
    road_info[b].append((cost, a))

print(solution(road_info, 1, n))

## 왜#때문에 무한루프,,
## 다익스트라 => heapq (우선순위큐)
