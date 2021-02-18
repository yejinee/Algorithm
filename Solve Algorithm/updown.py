"""
[ 이코테 - 상하좌우 ]
여행가 A는 N*N 크기의 정사각형 공간 위에 서 있습니다.
이 공간은 1*1 크기의 정사각형으로 나누어져 있습니다.
가장 왼쪽 위 좌표는 (1,1)이며, 가장 오른쪽 아래 좌표는 (N,N)에 해당
여행가 A는 상,하,좌,우 방향으로 이동 가능 & 시작 좌표: (1,1)
이동시 범위 벗어나면 그 명령은 수행 불가

계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L,R,U,D 중 하나의 문자가 반복적으로 적혀 있음
L: 왼쪽으로 한칸 이동
R: 오른쪽으로 한 칸 이동
U: 위로 한 칸 이동
D: 아래로 한 칸 이동

[ input ]
첫째 줄에 공간의 크기 나타내는 N 주어짐 (1<=N<=100)
둘째 줄에 여행가 A가 이동할 계획서의 내용이 주어짐 (1<=이동 횟수<=100)

[ output ]
첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표 (X,Y)를 공백을 기준으로 구분하여 출력

[ Solution]
명령에 따라 이동 => 시뮬레이션 
"""
# L,R,U,D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def solution(n, plan):
    x, y = 1, 1
    move = ['L', 'R', 'U', 'D']
    for p in plan:
        for m in range(len(move)):
            # 일치하는 문자에 대해 이동
            if p == move[m]:
                nx = x+dx[m]
                ny = y+dy[m]
        # 범위 확인 해보기
        if nx < 1 or nx > n or ny < 1 or ny > n:
            continue
        x, y = nx, ny
        print(x, y)
    return x, y


N = int(input())
plan = list(input().split())
print(solution(N, plan))
