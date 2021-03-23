"""
[ 14502. 연구소 ]


[ input ]
첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)

둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 
2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.

빈 칸의 개수는 3개 이상이다.

[ output ]
첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.

"""
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def virus(x, y):  # 바이러스의 위치 알 때 번식후에는?
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            # 번식이 가능한 경우
            if after[nx][ny] == 0:
                after[nx][ny] = 2
                virus(nx, ny)


def safeplace():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if after[i][j] == 0:
                cnt += 1

    return cnt


def solution(cnt):  # virus갯수 count
    global result
    if cnt == 3:
        #벽 만들고 나서의 board (새로 만들어주기)
        for i in range(n):
            for j in range(m):
                after[i][j] = board[i][j]
        # 바뀐 board에 대해 virus증식하면 어떻게 되는지 구하기
        for i in range(n):
            for j in range(m):
                if after[i][j] == 2:
                    virus(i, j)
        result = max(result, safeplace())
        return

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:  # 빈칸인 경우
                board[i][j] = 1  # 벽 만들어 주기
                cnt += 1
                solution(cnt)
                board[i][j] = 0
                cnt -= 1


n, m = map(int, input().split())
board = []
after = [[0]*m for _ in range(n)]
result = 0
for _ in range(n):
    board.append(list(map(int, input().split())))

solution(0)
print(result)
