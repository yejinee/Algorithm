"""
[ 이코테 - 볼링공 고르기 ]
"""


def solution(n, m, k):
    weight = [0]*11  # 무게에 대한 갯수(M의 최댓값:10)
    cnt = 0
    for i in k:
        weight[i] += 1
    for w in range(1, m+1):
        n -= weight[w]  # 나머지 볼링공 갯수
        cnt += weight[w]*n  # 해당 무게의 볼링공 갯수 * 나머지 볼링공의 갯수
    return cnt


n, m = map(int, input().split())
K = list(map(int, input().split()))
print(solution(n, m, K))
