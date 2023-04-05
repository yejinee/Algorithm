"""
[ 2504. 괄호의 값 ]
- Stack 사용

- i) '('인 경우 => amount*2 & stack에 추가
- ii) '['인 경우 => amount*3 & stack에 추가
- iii) ')'인 경우 
    - stack이 비어있는 경우 => return 0
    - stack에서의 전 값이 '['인 경우 => return 0
    - 문자열 전 값이 '('인 경우 => ans에 더해줌 
        - (왜 stack전 값 비교하면 안되는가? stack값을 가지고 계산하면 중복 계산이 됨 )
        - 예를 들어, ([]) => 2*3 = 6이어야하는데 6+2가 됨 => 그러므로, ()는 계산 안해줘도 된다
    => //2해주기 (원래대로 돌아가기) & 짝이 맞았으니 pop
- iv) ']'인 경우
    - stack이 비어있는 경우 => return 0
    - stack에서의 전 값이 '('인 경우 => return 0
    - 문자열 전 값이 '['인 경우 => ans에 더해줌
    => //3해주기 (원래대로 돌아가기) & 짝이 맞았으니 pop
"""

def solution(str):
    stack = []
    mul_amt = 1
    ans = 0

    for idx, value in enumerate(str):
        if value=='(':
            mul_amt *= 2
            stack.append(value)
        elif value=='[':
            mul_amt *= 3
            stack.append(value)


        elif value == ')':
            if not stack or stack[-1]=='[':
                return 0
            if stack[-1]=='(':
                ans += mul_amt
            mul_amt //= 2
            stack.pop()

        else:
            if not stack or stack[-1]=='(':
                return 0
            if stack[-1]=='[':
                ans += mul_amt
            mul_amt //= 3
            stack.pop()

    if stack:
        return 0

    return ans
                            

str = input()
print(solution(str))