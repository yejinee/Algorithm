dx = [0,0,1,-1]
dy = [1,-1,0,0]

def solution():
    global max_value
    # dfs 진행
    for i in range(n):
        for j in range(m):
            visited[i][j] = True
            # (i,j)을 기준점으로 시작해서 테트로미노(ㅗ제외)로 구할 수 있는 최대값 계산
            dfs(i,j,board[i][j], 1)
            visited[i][j] = False

            # (i,j)을 기준점으로 시작해서 테트로미노(ㅗ)로 구할 수 있는 최대값 계산
            max_f(i, j)


def dfs(i, j, tsum, cnt):
    """
    [ 테트로미노(ㅗ제외)의 최대값 ]
    - (i,j)을 기준점으로 시작해서 테트로미노(ㅗ제외)로 구할 수 있는 최대값 계산
    - IDEA : ㅗ 제외한 다른 블록들은 4개점 연속 잇다 보면 무조건 나옴
    """
    global max_value
    # out:
    if cnt == 4:
        max_value = max(max_value, tsum)
        return 
    # 시작점에서부터 이동
    for k in range(4):
        ni, nj = i+dx[k], j+dy[k]
        if 0<=ni<n and 0<=nj<m and not visited[ni][nj]:
            visited[ni][nj] = True
            dfs(ni, nj, tsum+board[ni][nj], cnt+1)
            visited[ni][nj] = False


def max_f(i, j):
    """
    [ 테트로미노(ㅗ)의 최대값 ]
    - (i,j)을 기준점으로 시작해서 테트로미노(ㅗ)로 구할 수 있는 최대값 계산
    - 가운데점 기준으로 계산
    """
    global max_value
    for type in range(4):
        tsum = board[i][j]

        for direction in range(3):
            # 가운데점 기준으로 3개방향만 체크
            d_idx = (type + direction) % 4
            ni, nj = i+dx[d_idx], j+dy[d_idx]
            if not (0<=ni<n and 0<=nj<m):
                tsum = 0
                break
            tsum += board[ni][nj]

        max_value = max(max_value, tsum)


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
max_value = 0
visited = [[False]*m for _ in range(n)]

solution()

print(max_value)