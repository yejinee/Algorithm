from collections import deque
dx = [0, 0, -1, 1]
dy = [-1 ,1, 0, 0]

def bfs(i, j):
    group = []
    q = deque()
    q.append([i, j])
    group.append([i, j])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if L <= abs(board[nx][ny]-board[x][y]) <= R:
                    group.append([nx, ny])
                    q.append([nx, ny])
                    visited[nx][ny] = 1
    return group


N, L, R = map(int, input().split())
board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

day = 0
while True:
    visited = [[0]*N for _ in range(N)]
    finalflag = False

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                # 열린 국경선 체크하고 위치 반환
                group = bfs(i,j)

                # 국경이 열린 나라들의 인구를 update
                if len(group) > 1:
                    finalflag = True
                    change_value = sum([board[x][y] for x,y in group]) // len(group)
                    for x, y in group:
                        board[x][y] = change_value
    # 국경이 열리지 않을 때까지 반복
    if not finalflag:
        break
    day+=1

print(day)
