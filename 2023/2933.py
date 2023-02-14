from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def solution(numbers, height):
    """
    [ 해결 IDEA ]
    1. 던진다 
	    a. 짝수면 왼쪽 -> 오른쪽, 홀수면 오른쪽 -> 왼쪽
	2. 미네랄이 파괴되는 경우
		a. 떠있는 클러스터를 확인한다 (BFS => 오래걸릴듯? / pass)
		b. 상하좌우에 미네랄 확인하기 => 낙하할 수 있는 후보로 선정
	3. 분리된 클러스터는 밑으로 내려주기
		a. 각 클러스터에 대해서 bfs => 최저 y좌표 구하기
        b. Y좌표가 0이 아니면 => 낙하
    """

    for number in range(numbers):
        # 1. 막대기 던지기
        throw()
        # 2. 클러스터 확인
        check_cluster()
        # 3. 낙하
        get_min_column() # 최저 y좌표
        get_fall_height()   # 내릴 높이 구하기
        fall()  # 내리기
        


def throw(x, number):
    """
    [ 1. 막대기 던지기 Function ]
    - 짝수면 왼쪽 -> 오른쪽, 홀수면 오른쪽 -> 왼쪽
    """
    if number%2 == 0:
        for y in range(c):
            if board[x][y] == 'x':
                board[x][y] = '.'
                break
    else:
        for y in range(c-1, -1, -1):
            if board[x][y] == 'x':
                board[x][y] = '.'
                break

def check_cluster():
    """
    [ 2. 클러스터 확인 Function ]
        - BFS를 통해 클러스터 확인    
    
    """
    q = deque()
    cluster_info = [[0] * c for _ in range(r)]

    # BFS를 통해 클러스터 확인
    cluster_no = 1
    for i in range(r):
        for j in range(c):
            if cluster_info[i][j] == 0:
                if board[i][j] == 'x':  # 미네랄들만 탐색해서 클러스터 계산
                    # initialize
                    q.append((i,j))
                    cluster_info[i][j] = cluster_no
                    # bfs
                    while q:
                        x, y = q.popleft()
                        for k in range(4):
                            nx, ny = x+dx[k], y+dy[k]
                            # check range
                            if 0<=nx<r and 0<=ny<c:
                                # not visited & mineral
                                if cluster_info[nx][ny] == 0 and board[nx][ny] == 'x':
                                    q.append((nx, ny))
                                    cluster_info[nx][ny] = cluster_info[x][y]               
                    cluster_no += 1


def get_min_column(cluster_info):
    """
    [ 3. 최저 y좌표 구하기 Function ]
    """
    # 최저 y좌표 구하기
    min_y_info = [-1] * c
    for x in range(c):
        for y in range(r-1, -1, -1):
            if cluster_info[y][x]:
                min_y_info[x] = y
                break
    
    return min_y_info

def get_fall_height(min_y_info):
    """
    얼마나 내릴 수 있는지 체크
    """
    for x, min_y in enumerate(min_y_info):
        # 아무것도 내릴 게 없는 경우
        if min_y == -1:
            continue
        # 얼마나 내릴 수 있는지 측정
        for y in range(min_y+1, r):
            # 밑에 미네랄 있는 경우
            if board[y][x] == 'x':
                min_diff = min(min_diff, y-min_y-1)
                break
            # 바닥인 경우
            if y==r-1:
                min_diff = min(min_diff, y-min_y)
    return min_diff

def fall():
    """
    낙하시키는 함수
    """
    for y in range(r-1, -1, -1):
        for x in range(c):
            if not cluster_info[y][x]:
                continue
            board[y][x] = '.'
            board[y+h][x] = 'x'


r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
n = int(input())
h = list(map(int, input().split()))



