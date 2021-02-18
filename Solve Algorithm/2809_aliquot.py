"""
약수 구하기 -> 에라토스체네스의 체 사용 

<에라토스체네스의 체>
보통 소수 구할때 사용
: 100이하의 소수 찾고 싶으면 100의 제곱근이 10이하의 소수에 대해서만 반복

"""
import math
N=int(input())
result=[]
length=int(math.sqrt(N))
for i in range(1,length+1) :
    if N%i==0:
        result.append(i)
        if i!=N//i:   #똑같은 수 두번 출력 방지
            result.append(N//i)
result.sort()
print(' '.join(map(str,result)))  #[] 없애고 출력하기 