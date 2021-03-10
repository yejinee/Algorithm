"""
[ 이코테 - 금광 ]
"""


def solution(n, m, case):
    d = []
    for i in range(n):
        d.append(case[i*m:i*m+m])

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = d[i-1][j-1]

            if i == n-1:
                left_down = 0
            else:
                left_down = d[i+1][j-1]
            d[i][j] = max(left_up, d[i][j-1], left_down)+d[i][j]
    ans = 0
    for i in range(n):
        ans = max(ans, d[i][m-1])

    return ans


T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    case = list(map(int, input().split()))
    print(solution(n, m, case))
