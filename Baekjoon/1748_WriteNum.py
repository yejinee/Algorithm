"""
1부터 N까지의 수를 이어서 쓰면 다음과 같이 새로운 하나의 수를 얻을 수 있다.

1234567891011121314151617181920212223...

이렇게 만들어진 새로운 수는 몇 자리 수일까? 이 수의 자릿수를 구하는 프로그램을 작성하시오.

[ input ]
첫째 줄에 N(1≤N≤100,000,000)이 주어진다.

[ output ]
첫째 줄에 새로운 수의 자릿수를 출력한다.

[ solution ]
# 1 자리 : 1~ 9 : 9개
# 2 자리 : 10 ~  99 : 90개
# 3 자리 : 100 ~ 999: 900개
# 4 ; 1000 ~ 9999: 9000개

N=120인 경우) 
1~9 : 길이 1 -> 9개 
10~99: 길이 2 -> 90개
100~120: 길이 3 -> 21개
ans= (10-1+1)*1+(99-10+1)*2+(120-100+1)*3

"""


def solution(n):
    ans = 0
    start = 1
    length = 1
    while start <= n:
        end = start*10-1
        if end > n:
            end = n
        ans += (end-start+1)*length
        start *= 10
        length += 1
    return ans


N = int(input())
print(solution(N))

