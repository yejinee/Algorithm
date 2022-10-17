import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def solution(n, graph):
    distance = [[INF]*(n) for _ in range(n)]
    hq = []
    heapq.heappush(hq, [graph[0][0], 0, 0])
    distance[0][0] = 0


    while hq:
        now_cost, x, y = heapq.heappop(hq)

        if (x == n-1) and (y == n-1):
            return distance[n-1][n-1]

        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if (0<=nx<n) and (0<=ny<n):
                new_cost = graph[nx][ny] + now_cost
                if distance[nx][ny] > new_cost:
                    distance[nx][ny] = new_cost
                    heapq.heappush(hq, (new_cost, nx, ny))

cnt = 1
while True:
    graph = []
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        graph.append(list(map(int, input().split())))
    print("Problem {}: {}".format(cnt, solution(n, graph)))
    cnt += 1