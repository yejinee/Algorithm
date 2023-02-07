from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

dx = (0,1,0,-1)
dy = (1,0,-1,0)

def solution(sx, sy, ex, ey):
    q = deque()
    visited = [[[INF]*4 for _ in range(w)] for _ in range(h)]   # 방향까지

    # initialize (시작점 기준 상하좌우 중 벽이 아닌 곳의 좌표를 모두 저장)
    for k in range(4):
        nx, ny = sx + dx[k], sy + dy[k]
        if 0<=nx<h and 0<=ny<w and board[nx][ny] != "*":
            q.append((nx, ny, k))
            visited[nx][ny][k] = 0
            
    while q:
        x, y, direct = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0<=nx<h and 0<=ny<w and board[nx][ny] != "*":
                cnt = visited[x][y][direct] # 현재까지 방향 바꾸는 횟수
                # 방향을 틀어야하는 경우
                if direct == 0 or direct == 2:
                    if k == 1 or k == 3:
                        cnt += 1
                else:
                    if k == 0 or k == 2:
                        cnt += 1
                
                # 방문한 적 없는 경우
                if visited[nx][ny][k] == -1 :
                    visited[nx][ny][i] = cnt
                    q.append((nx, ny, k))
                else:
                    # 방문했지만, 이전 거울갯수보다 최소인 경우
                    if visited[nx][ny][k] > cnt:
                        visited[nx][ny][k] = cnt
                        q.append((nx, ny, k))
    return min(visited[ex][ey])
                
    

w, h = map(int, input().split())
board, point = [], []

for i in range(h):
    board.append(list(str(input().strip())))
    # find C location (시간에러나면 이거 변경)
    for j in range(w):
        if board[i][j] == 'C':
            point.append((i,j))

# print(board)
print(solution(point[0][0], point[0][1], point[1][0], point[1][1]))