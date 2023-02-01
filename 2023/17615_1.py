# 이 코드는 29점 => 같은 코드이지만 strip/count 사용하지 말고 짤 것
def solution(ball):
    """
    최소이동횟수 계산 funtion
    - Greedy Algorithm 사용
    1. 좌/우 한쪽으로 몰려있는 공 제거
    2. 나머지 배열에 있는 R/B 공을 좌우측으로 몰아 줄때의 횟수 계산
    """
    move_cnt = []

    ## R이 우측에 몰려있는 경우 & 남은 공 중 R의 갯수
    move_cnt.append(ball.rstrip('R').count('R'))
    ## B이 우측에 몰려있는 경우 & 남은 공 중 B의 갯수
    move_cnt.append(ball.rstrip('B').count('B'))
    ## R이 좌측에 몰려있는 경우 & 남은 공 중 R의 갯수
    move_cnt.append(ball.lstrip('R').count('R'))
    ## B이 좌측에 몰려있는 경우 & 남은 공 중 B의 갯수
    move_cnt.append(ball.rstrip('B').count('B'))

    return min(move_cnt)


n = int(input())
ball = input()

print(solution(ball))
