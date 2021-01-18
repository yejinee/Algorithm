"""
스타트링크에서 판매하는 어린이용 장난감 중에서 가장 인기가 많은 제품은 구슬 탈출이다. 
구슬 탈출은 직사각형 보드에 빨간 구슬과 파란 구슬을 하나씩 넣은 다음, 빨간 구슬을 구멍을 통해 빼내는 게임이다.

보드의 세로 크기는 N, 가로 크기는 M이고, 편의상 1×1크기의 칸으로 나누어져 있다. 
가장 바깥 행과 열은 모두 막혀져 있고, 보드에는 구멍이 하나 있다. 
빨간 구슬과 파란 구슬의 크기는 보드에서 1×1크기의 칸을 가득 채우는 사이즈이고, 각각 하나씩 들어가 있다. 
게임의 목표는 빨간 구슬을 구멍을 통해서 빼내는 것이다. 
이때, 파란 구슬이 구멍에 들어가면 안 된다.

이때, 구슬을 손으로 건드릴 수는 없고, 중력을 이용해서 이리 저리 굴려야 한다.
왼쪽으로 기울이기, 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기와 같은 네 가지 동작이 가능하다.

각각의 동작에서 공은 동시에 움직인다. 
빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패이다. 
빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다. 
빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다. 
또, 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다. 기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다.

보드의 상태가 주어졌을 때, 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하는 프로그램을 작성하시오.

[ input ]
첫 번째 줄에는 보드의 세로, 가로 크기를 의미하는 두 정수 N, M (3 ≤ N, M ≤ 10)이 주어진다. 
다음 N개의 줄에 보드의 모양을 나타내는 길이 M의 문자열이 주어진다. 
이 문자열은 '.', '#', 'O', 'R', 'B' 로 이루어져 있다. 
'.'은 빈 칸을 의미하고, '#'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며, 'O'는 구멍의 위치를 의미한다. 
'R'은 빨간 구슬의 위치, 'B'는 파란 구슬의 위치이다.

입력되는 모든 보드의 가장자리에는 모두 '#'이 있다. 
구멍의 개수는 한 개 이며, 빨간 구슬과 파란 구슬은 항상 1개가 주어진다.


[ output ]
최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 출력한다. 
만약, 어떻게 움직여도 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1을 출력한다.

"""

from collections import deque
import copy
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 구슬을 한방향으로 움직이지 않을때까지 기울임
def stimulate(a, direction, x, y):
    if a[x][y] == '.':  # 더이상 이동 불가
        return (False, False, x, y)
    n = len(a)  # 행의 갯수
    m = len(a[0])  # 열의 갯수
    moved = False 
    while True:
        nx, ny = x+dx[direction], y+dy[direction]  # 이동하기
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            return(moved, False, x, y)
        if a[nx][ny] == '#':  # 벽인경우 -> 이동 불가능
            return(moved, False, x, y)
        elif a[nx][ny] in 'RB': # 다른 구슬이 있는 경우 -> 이동 불가
            return (moved, False, x, y)
        elif a[nx][ny] == '.':  # 빈칸인 경우에 계속 이동해야하므로 return 없음
            a[x][y], a[nx][ny] = a[nx][ny], a[x][y]
            x, y = nx, ny
            moved = True
        elif a[nx][ny] == 'O': # 구멍인 경우
            a[x][y] = '.'
            moved = True 
            return(moved, True, x, y)

# 구슬이 이동한 뒤의 상태 반환 함수
def go(a, rx, ry, bx, by, direction):
    b = copy.deepcopy(a)
    b[rx][ry] = 'R'
    b[bx][by] = 'B'
    hole1, hole2 = False, False
    while True:
        # x,y를 이동할만큼 전부 다 이동 (항상 red먼저 이동해줘야함)
        rmoved, rhole, rx, ry = stimulate(b, direction, rx, ry)
        bmoved, bhole, bx, by = stimulate(b, direction, bx, by)
        if rmoved==False and bmoved==False:
            break
        if rhole: # red가 움직인 경우
            hole1 = True
        if bhole: # blue가 움직인 경우 
            hole2 = True
    return (hole1, hole2, rx, ry, bx, by)


def BallExit(a, N, M):
    q = deque()
    # 보드에서 hole,red,blue 위치 찾기 
    for i in range(N):
        for j in range(M):
            if a[i][j] == 'O':
                hx, hy = i, j
            elif a[i][j] == 'R':
                rx, ry = i, j
                a[i][j] = '.'
            elif a[i][j] == 'B':
                bx, by = i, j
                a[i][j] = '.'
    q.append((rx, ry, bx, by))
    d = [[[[-1]*M for k in range(N)]for j in range(M)] for i in range(N)] # 몇 번 이동했는지 기록
    d[rx][ry][bx][by] = 0  # 시작점 0부터 시작
    ans = -1
    found = False # 구멍에 들어가면 true
    while q:
        rx, ry, bx, by = q.popleft()
        for k in range(4):
            hole1, hole2, nrx, nry, nbx, nby = go(a, rx, ry, bx, by, k)
            if hole2: # blue가 들어간 경우
                continue
            if hole1: # red가 들어간 경우
                found = True
                ans = d[rx][ry][bx][by]+1
                break
            if d[nrx][nry][nbx][nby] != -1:
                continue
            q.append((nrx, nry, nbx, nby))
            d[nrx][nry][nbx][nby] = d[rx][ry][bx][by]+1 # 이동할 곳 = 현 위치 + 1
        if found:
            break

    return ans


N, M = map(int, input().split())
a = [list(input()) for _ in range(N)]
print(BallExit(a, N, M))
