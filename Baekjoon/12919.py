"""
[ 12919. A와 B 2 ]
수빈이는 A와 B로만 이루어진 영어 단어 존재한다는 사실에 놀랐다. 
대표적인 예로 AB (Abdominal의 약자), BAA (양의 울음 소리), AA (용암의 종류), ABBA (스웨덴 팝 그룹)이 있다.

이런 사실에 놀란 수빈이는 간단한 게임을 만들기로 했다. 
두 문자열 S와 T가 주어졌을 때, S를 T로 바꾸는 게임이다. 
자열을 바꿀 때는 다음과 같은 두 가지 연산만 가능하다.

문자열의 뒤에 A를 추가한다.
문자열의 뒤에 B를 추가하고 문자열을 뒤집는다.
주어진 조건을 이용해서 S를 T로 만들 수 있는지 없는지 알아내는 프로그램을 작성하시오. 

[ input ]
첫째 줄에 S가 둘째 줄에 T가 주어진다. (1 ≤ S의 길이 ≤ 49, 2 ≤ T의 길이 ≤ 50, S의 길이 < T의 길이)

[ output ]
S를 T로 바꿀 수 있으면 1을 없으면 0을 출력한다.
"""
import sys
input = sys.stdin.readline

def check(S, T):
    global flag
    if len(T) == len(S):
        if T == S:
            flag = True
        return 
    
    # 첫 글짜가 B인 Case
    if T[0] == 'B':
        T.reverse()
        T.pop()
        check(S, T)
        T.append("B")
        T.reverse()
    # 마지막 글짜가 A인 Case
    if T[-1] == 'A':
        T.pop()
        check(S, T)
        T.append("A")
    

S = list(map(str, sys.stdin.readline().strip()))
T = list(map(str, sys.stdin.readline().strip()))
flag = False
check(S,T)

if flag : print(1)
else: print(0)

