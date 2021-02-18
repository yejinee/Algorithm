"""
[ 이코테 - 문자열 재정렬 ]
알파벳 대문자와 숫자(0-9)로만 구성된 문자열이 입력으로 주어짐
이때, 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤, 그 뒤에 더한 값을 이어서 출력

Ex) K1KA5CB7 -> ABCKK13

[ INPUT ]
첫째줄에 하나의 문자열 S주어짐 (1<=S의 길이<=10000)

[ OUTPUT ]
첫째 줄에 문제에서 요구하는 정답 출력

[ SOLUTION ]
    1. 문자 전부 살펴보기 (len(S), 최대여도 10000)
        if 문자면 list에 저장
        else 숫자인 경우 더해주기 
    2. 문자 list 정렬하기
    3. 숫자는 뒤에 붙여서 출력
"""


def solution(s):
    num = 0
    re = []
    # 문자열 전부 확인 
    for value in s:
        # 알파벳인 경우
        if value.isalpha():
            re.append(value)
        else: # 숫자인 경우
            num += int(value)
    # 문자열 정렬 
    re.sort()
    ans = ''.join(re)
    return ans+str(num)


S = input()
print(solution(S))
