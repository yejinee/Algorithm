"""
[ solution ]
- dp 이용
- S(x) : x를 1,2,3의 합으로 나타내는 갯수
    - S(1) = 1, S(2) = 2, S(3) = 3
    - n을 1로만 나타내는 경우 : 1가지
    - 마지막이 2인 경우: (n-2) + 2 => S(n-2)
    - 마지막이 3인 경우: (n-3) + 3 => S(n-3)
    So, S(n) = S(n-2) + S(n-3) + 1

    => 2차원 배열로 다시 풀 것ㄴ

"""
 

T = int(input())
ans = [int(input()) for _ in range(T)]

s = [1] * 10001
# 마지막이 2인 경우
for i in range(2, 10001):
    s[i] += s[i-2]
# 마지막이 3인 경우
for i in range(3, 10001):
    s[i] += s[i-3]

for v in ans:
    print(s[v])
