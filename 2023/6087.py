from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]
def solution(w, h, board):
    point = []
    # find C location
    for i in range(h):
        for j in range(w):
            if board[i][j] == 'C':
                point.append([i,j])


    visited = [[1e9]*w for _ in range(h)]
    sx, sy, ex, ey = point[0][0], point[0][1], point[1][0], point[1][1] 
    q = deque()
    q.append([sx, sy])
    visited[sx][sy] = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            while True:
                # 계속 한방향으로 전진
                ## 범위 벗어나는 경우
                if not (0<=nx<h and 0<=ny<w):
                    break
                ## 벽 만나는 경우 => 전진 금지
                if board[nx][ny] == '*':
                    break
                ## 이미 지난 적이 있음 & 전에 탐색한 루트가 더 좋은 경우
                if visited[nx][ny] < (visited[x][y] + 1):
                    break
            
                # move
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
                nx += dx[k]
                ny += dy[k]
    
    return visited[ex][ey]-1

w, h = map(int, input().split())
board = []
for _ in range(h):
    board.append(list(str(input())))
print(solution(w,h,board))