"""
[ 럭키 스트레이트 ]
어떤 게임의 아웃복서 캐릭터에게는 럭키 스트레이트라는 기술이 존재한다. 
이 기술은 매우 강력한 대신에 항상 사용할 수는 없으며, 현재 게임 내에서 점수가 특정 조건을 만족할 때만 사용할 수 있다.

특정 조건이란 현재 캐릭터의 점수를 N이라고 할 때 점수 N을 자릿수를 기준으로 반으로 나누어 
왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황을 의미한다. 
예를 들어 현재 점수가 123,402라면 왼쪽 부분의 각 자릿수의 합은 1+2+3, 오른쪽 부분의 각 자릿수의 합은 4+0+2이므로 
두 합이 6으로 동일하여 럭키 스트레이트를 사용할 수 있다.

현재 점수 N이 주어졌을 때, 럭키 스트레이트를 사용할 수 있는 상태인지 아닌지를 알려주는 프로그램을 작성하시오. 
럭키 스트레이트를 사용할 수 있다면 "LUCKY"를, 사용할 수 없다면 "READY"라는 단어를 출력한다. 
또한 점수 N의 자릿수는 항상 짝수 형태로만 주어진다. 
예를 들어 자릿수가 5인 12,345와 같은 수는 입력으로 들어오지 않는다.


[ input ]
첫째 줄에 점수 N이 정수로 주어진다. (10 ≤ N ≤ 99,999,999) 
단, 점수 N의 자릿수는 항상 짝수 형태로만 주어진다.

[ output ]
첫째 줄에 럭키 스트레이트를 사용할 수 있다면 "LUCKY"를, 사용할 수 없다면 "READY"라는 단어를 출력한다.

"""
def solution(N):
    nlist=[int(i) for i in str(N)] # 숫자로 자릿수 list 만들기 
    front=sum(nlist[:len(nlist)//2]) # 0~len(N)/2까지의 sum
    back=sum(nlist[len(nlist)//2:]) #len(N)/2 ~ 까지의 sum
    if front==back: # 앞뒤의 값 같은 경우 
        return "LUCKY"
    else:
        return "READY"

N=int(input())
print(solution(N))


