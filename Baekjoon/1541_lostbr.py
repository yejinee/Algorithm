"""
세준이는 양수와 +, -, 그리고 괄호를 가지고 길이가 최대 50인 식을 만들었다. 
그리고 나서 세준이는 괄호를 모두 지웠다.

그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.


[ INPUT ]
첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다. 
그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 
수는 0으로 시작할 수 있다.



[ OUTPUT ]
첫째 줄에 정답을 출력한다.


"""
import sys
input=sys.stdin.readline


def calculate(s):
    result=0 # 최솟값
    #제일 첫번째에 있는 value의 값 구하기
    for i in s[0].split('+'): # '+'를 기준으로 분해
        result+=int(i)
    # 두번째부터 끝까지 value들에 접근
    for i in s[1:]:
        one=0   # 하나의 value만 계산 
        for j in i.split('+'): #'+'를 기준으로 분해
            one+=int(j)
        result-=one
    return result


S=input().split('-') # '-'를 기준으로 list에 저장 
print(calculate(S))

