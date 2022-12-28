"""
[ 3197. 백조의 호수 ]
두 마리의 백조가 호수에서 살고 있었다. 그렇지만 두 마리는 호수를 덮고 있는 빙판으로 만나지 못한다.

호수는 행이 R개, 열이 C개인 직사각형 모양이다. 어떤 칸은 얼음으로 덮여있다.

호수는 차례로 녹는데, 매일 물 공간과 접촉한 모든 빙판 공간은 녹는다. 두 개의 공간이 접촉하려면 가로나 세로로 닿아 있는 것만 (대각선은 고려하지 않는다) 생각한다.

아래에는 세 가지 예가 있다.

...XXXXXX..XX.XXX ....XXXX.......XX .....XX.......... 
....XXXXXXXXX.XXX .....XXXX..X..... ......X.......... 
...XXXXXXXXXXXX.. ....XXX..XXXX.... .....X.....X..... 
..XXXXX..XXXXXX.. ...XXX....XXXX... ....X......XX.... 
.XXXXXX..XXXXXX.. ..XXXX....XXXX... ...XX......XX.... 
XXXXXXX...XXXX... ..XXXX.....XX.... ....X............ 
..XXXXX...XXX.... ....XX.....X..... ................. 
....XXXXX.XXX.... .....XX....X..... ................. 
      처음               첫째 날             둘째 날
백조는 오직 물 공간에서 세로나 가로로만(대각선은 제외한다) 움직일 수 있다.

며칠이 지나야 백조들이 만날 수 있는 지 계산하는 프로그램을 작성하시오.

[ input ]
입력의 첫째 줄에는 R과 C가 주어진다. 단, 1 ≤ R, C ≤ 1500.

다음 R개의 줄에는 각각 길이 C의 문자열이 하나씩 주어진다. 
'.'은 물 공간, 'X'는 빙판 공간, 'L'은 백조가 있는 공간으로 나타낸다.


[ output ]
첫째 줄에 문제에서 주어진 걸리는 날을 출력한다.

"""
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def find_swan(swan_q, swan, visited, board):
    swan_nextq = deque()    # 백조가 얼음발견 시 값 저장 queue
    while swan_q:
        y, x = swan_q.popleft()
        if y == swan[1][0] and x == swan[1][1]: # 다른 백조를 만나는 경우
            return True, None
        # 다른 백조를 만나지 못하는 경우 
        for k in range(4):
            ny, nx = y+dy[k], x+dx[k]
            if (0<=ny<r) and (0<=nx<c) and (visited[ny][nx]==False):
                # 얼음이면 nextq에 저장
                if board[ny][nx] == 'X':
                    swan_nextq.append([ny, nx])
                # 물인 경우 계속 bfs진행
                else:
                    swan_q.append([ny,nx])
                visited[ny][nx] = True
    return False, swan_nextq

def melt_ice(water_q, board):
    water_nextq = deque()
    # 물의 위치 주변을 탐색
    while water_q:
        y, x = water_q.popleft()
        for k in range(4):
            ny, nx = y+dy[k], x+dx[k]
            if 0<=ny<r and 0<=nx<c:
                # 얼음인 경우 다음 탐색 대상으로 저장
                if board[ny][nx] == 'X':
                    water_nextq.append([ny,nx])
                    board[ny][nx] = '.'
    return water_nextq

def solution(board):
    water_q = deque()
    swan = []
    day = -1
    visited = [[False for _ in range(c)] for _ in range(r)]

    # board 위치 초기화 (물,백조)
    for row in range(r):
        for col, val in enumerate(board[row]):
            if val == '.' or val == 'L':
                water_q.append([row, col])
            if val == 'L':
                swan.append([row, col])

    # 백조의 위치 초기화
    swan_q = deque() # 백조가 다른백조 찾을때 사용
    y, x = swan[0][0], swan[0][1]
    swan_q.append([y,x])
    visited[y][x] = True

    while True:
        day += 1
        found_flag, swan_nextq = find_swan(swan_q, swan, visited, board)
        if found_flag: break
        water_q = melt_ice(water_q, board)
        swan_q = swan_nextq

    return day


r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
print(solution(board))