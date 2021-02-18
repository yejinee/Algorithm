"""
[ 이코테- 시각 ]
정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 
모든 경우의 수를 구하는 프로그램 작성하기
Ex) 1을 입력했을 때 
    세어야 하는 시각  => 00시00분03초 , 00시 13분 30초
    세면 안되는 시각  => 00시02분55초 , 01시 27분 45초 
[ input ]
첫째 줄에 정수N 입력

[ output ]
00시00분00초 부터 N시59분59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수 출력

[ solution ]
전부 확인하면 => 00:00:00 ~ 23:59:59 이므로 24*60*60=86400
Brutr Force로 풀어주기 
"""


def solution(n):
    cnt = 0
    for h in range(n+1):
        for m in range(60):
            for s in range(60):
                # 3이 있나 확인
                if '3' in str(h)+str(m)+str(s):
                    cnt += 1
    return cnt


N = int(input())
print(solution(N))
