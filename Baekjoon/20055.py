"""
[ 20055. 컨베이어 벨트 위의 로봇 ]
길이가 N인 컨베이어 벨트가 있고, 길이가 2N인 벨트가 이 컨베이어 벨트를 위아래로 감싸며 돌고 있다. 벨트는 길이 1 간격으로 2N개의 칸으로 나뉘어져 있으며, 각 칸에는 아래 그림과 같이 1부터 2N까지의 번호가 매겨져 있다.


벨트가 한 칸 회전하면 1번부터 2N-1번까지의 칸은 다음 번호의 칸이 있는 위치로 이동하고, 2N번 칸은 1번 칸의 위치로 이동한다. i번 칸의 내구도는 Ai이다. 위의 그림에서 1번 칸이 있는 위치를 "올리는 위치", N번 칸이 있는 위치를 "내리는 위치"라고 한다.

컨베이어 벨트에 박스 모양 로봇을 하나씩 올리려고 한다. 로봇은 올리는 위치에만 올릴 수 있다. 언제든지 로봇이 내리는 위치에 도달하면 그 즉시 내린다. 로봇은 컨베이어 벨트 위에서 스스로 이동할 수 있다. 로봇을 올리는 위치에 올리거나 로봇이 어떤 칸으로 이동하면 그 칸의 내구도는 즉시 1만큼 감소한다.

컨베이어 벨트를 이용해 로봇들을 건너편으로 옮기려고 한다. 로봇을 옮기는 과정에서는 아래와 같은 일이 순서대로 일어난다.

벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
종료되었을 때 몇 번째 단계가 진행 중이었는지 구해보자. 가장 처음 수행되는 단계는 1번째 단계이다.

[ input ]
첫째 줄에 N, K가 주어진다. 둘째 줄에는 A1, A2, ..., A2N이 주어진다.

[ output ]
몇 번째 단계가 진행 중일때 종료되었는지 출력한다.

"""
def rotate_belt():
    global n, k, A, robot
    # 내구도 list 회전
    A_end = A.pop()
    A.insert(0, A_end)
    # 내리는 위치에 로봇있을때 로봇을 내려주기
    if n-2 in robot:
        robot.remove(n-2)
    # 로봇 위치 회전
    for r in range(len(robot)):
        next_idx = (robot[r]+1)
        robot[r] = next_idx 

def rotate_robot():
    global n, k, A, robot
    # 내리는 위치에 로봇있을때 로봇을 내려주기
    if (n-2 in robot) and (n-1 not in robot) and (A[n-1]>=1):
        A[n-1] -= 1
        robot.remove(n-2)

    # 로봇 위치 변경
    for r in range(len(robot)):
        next_idx = (robot[r]+1)%(2*n)
        # 다음 이동 위치에 로봇이 없고 & 내구도 1이상 => 이동
        if (next_idx not in robot) and (A[next_idx]>=1):
            robot[r] = next_idx
            A[next_idx] -= 1

def new_robot():
    global n, k, A, robot
    # 올리는 위치에 로봇이 없고 & 내구도 0보다 크면 => 새로운 로봇 놓기
    if (0 not in robot) and (A[0]>0):
        robot.append(0)
        A[0] -= 1

def check_A():
    global n, k, A, robot
    cnt = 0
    # 내구도 0인 칸의 갯수가 k개 이상인지 check
    for a in A:
        if a == 0:
            cnt += 1
    if cnt >= k:
        return True

    return False

def solution():
    global n, k, A, robot
    cnt = 0
    while not check_A():
        # 1. 밸트 회전
        rotate_belt()
        # 2. 로봇 회전
        rotate_robot()
        # 3. 새로운 로봇 놓기
        new_robot()
        # 1회전 완료
        cnt += 1
    return cnt


n, k = map(int, input().split())
A = list(map(int, input().split()))
robot = []
print(solution())