"""
N×M의 행렬로 표현되는 맵이 있다. 
맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

[ input ]
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 
다음 N개의 줄에 M개의 숫자로 맵이 주어진다. 
(1, 1)과 (N, M)은 항상 0이라고 가정하자.


[ output ]
첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.


"""
from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
dq = deque()
dist = [[[0]*2 for _ in range(m)] for _ in range(n)]

# initialize
dist[0][0][0] = 1
dq.append((0, 0, 0))

while dq:
    x, y, k = dq.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            # 빈 방인 경우 & 방문한 적 X
            if a[nx][ny] == 0 and dist[nx][ny][k] == 0:
                dist[nx][ny][k] = dist[x][y][k]+1
                dq.append((nx, ny, k))
            # 방이 있는 경우 ( 벽을 부순적 없어야함 )
            if k == 0 and a[nx][ny] == 1 and dist[nx][ny][k+1] == 0:
                dist[nx][ny][k+1] = dist[x][y][k]+1
                dq.append((nx, ny, k+1))


if dist[n-1][m-1][0] != 0 and dist[n-1][m-1][1] != 0:
    print(min(dist[n-1][m-1]))
elif dist[n-1][m-1][0] != 0:
    print(dist[n-1][m-1][0])
elif dist[n-1][m-1][1] != 0:
    print(dist[n-1][m-1][1])
else:
    print(-1)
