"""
[ 이코테 - 왕실의 나이트 ]
왕실 정원은 8*8 좌표 평면임
정원의 특정한 한 칸에 나이트가 서 있다. 
나이트는 말을 타고 있기 때문에 이동시에는 L자 형태로만 이동 가능 & 정원 밖으로 나갈 수 X
- 이동 방식 
    1) 수평으로 2칸 이동 -> 수직으로 1칸 이동
    2) 수직으로 2칸 이동 -> 수평으로 1칸 이동 

나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수 출력

[ input ]
첫째 줄에 나이트가 위치한 곳의 좌표 나타내는 문자열 입력 
행 : a ~ h   열: 1 ~ 8

[ output ]
첫째 줄에 나이트가 이동할 수 있는 경우의 수 출력 
"""
dx = [-1, 1, -1, 1, -2, 2, -2, 2]
dy = [-2, -2, 2, 2, -1, -1, 1, 1]


def solution(night):
    cnt = 0
    x = int(night[1])
    y = int(ord(night[0]))-int(ord('a'))+1  # 아스키 코드로 변환해서 숫자 계산
    # 모든 방향으로 이동해보면서 범위 벗어나지 않는지 check
    for k in range(8):
        nx = x+dx[k]
        ny = y+dy[k]
        if nx < 1 or nx >= 8 or ny < 1 or ny >= 8:
            continue
        cnt += 1
    return cnt


night = input()
print(solution(night))
