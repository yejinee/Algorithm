def solution(ball):
    """
    최소이동횟수 계산 funtion
    - Greedy Algorithm 사용
    1. 좌/우 한쪽으로 공 몰 때의 횟수 구하기
        - 같은 색 공인 경우 => 넘어가기
        - 다른 색 공인 경우 => 같은 색 공 뭉텅이랑 건너뛰기
    """
    move_cnt = []

    ## 우측에 R공을 몰아넣는 case
    rball_cnt = 0
    case1_cnt = 0
    
    for i in range(len(ball)):
        if ball[i] == 'R':
            rball_cnt += 1
        if ball[i] == 'B' and rball_cnt:
            case1_cnt += 1
    move_cnt.append(case1_cnt)

    ## 우측에 B공을 몰아넣는 case
    bball_cnt = 0
    case2_cnt = 0
    
    for i in range(len(ball)):
        if ball[i] == 'B':
            bball_cnt += 1
        if ball[i] == 'R' and bball_cnt:
            case2_cnt += 1
    move_cnt.append(case2_cnt)

    ## 좌측에 R공을 몰아넣는 case
    rball_cnt = 0
    case3_cnt = 0
    ball.reverse()
    
    for i in range(len(ball)):
        if ball[i] == 'R':
            rball_cnt += 1
        if ball[i] == 'B' and rball_cnt:
            case3_cnt += 1
    move_cnt.append(case3_cnt)


    ## 좌측에 B공을 몰아넣는 case
    bball_cnt = 0
    case4_cnt = 0
    
    for i in range(len(ball)):
        if ball[i] == 'B':
            bball_cnt += 1
        if ball[i] == 'R' and bball_cnt:
            case4_cnt += 1
    move_cnt.append(case4_cnt)

    return min(move_cnt)



n = int(input())
ball = list(input())

print(solution(ball))
