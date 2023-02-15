from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

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
        - 결과는 dict형태로 반환
    """
    q = deque()
    cluster_info = [[0] * c for _ in range(r)]
    result = dict()

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


    # Dict 형태로 변환
    for i in range(r):
        for j in range(c):
            if cluster_info[i][j] != 0:
                # cluster 번호가 dict에 이미 key로 있다면
                if cluster_info[i][j] in result:
                    result[check_cluster[i][j]].append((i, j))
                else:
                    result[check_cluster[i][j]] = [(i,j)]
    return result, check_cluster


def falling(cluster_dict, check_cluster):
    # 낙하 할 높이 계산
    dist = [1e9] * (max(cluster_dict.key())+1)
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'x':
                x, y = i-1, j
                height = 1
                meet = False

                while 0<=x<n:
                    if board[x][y] == 'x':
                        meet = True
                        break
                    else:
                        x -= 1
                        height += 1
    # 발견된 미네랄이 다른 클러스터에 속하는지 체크
    if meet:
        if check_cluster[x][y] != check_cluster[i][j]:
            dist[check_cluster[x][y]] = min(dist[check_cluster[x][y]], height)


    # 클러스터가 바닥에 붙어있는지 체크 & 예외처리
    for cluster_no in cluster_dict:
        cluster_dict[cluster_no].sort(reversed = True)
        if cluster_dict[cluster_no][0][0] ==  r-1:
            continue
        for location in cluster_dict[i]:
            x, y = location
            dist[check_cluster[x][y]] = min(dist[check_cluster[x][y]], r-x)

            # 낙하하는 그룹인 경우
            if dist[check_cluster[x][y]] == 1e9:
                board[x][y] = '.'
                h = dist[check_cluster[x][y]]-1
                board[x+h][y]='x'



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
        throw(n-h[number], number)
        # 2. 클러스터 확인
        cluster_dict, check_cluster = check_cluster()
        # 3. 낙하
        falling(cluster_dict, check_cluster)

    # 정답 출력
    for i in board:
        print(''.join(i))



r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
n = int(input())
h = list(map(int, input().split()))

solution(n, h)
